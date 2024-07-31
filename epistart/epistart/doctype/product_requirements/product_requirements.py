import frappe
from frappe import _
from frappe.model.document import Document


class ProductRequirements(Document):
    def validate(self):
        self.sync_product_features_with_tasks()

    @frappe.whitelist()
    def sync_activities_with_tasks(self):
        if not self.project:
            return False

        try:
            project_tasks = frappe.get_all(
                "Task",
                filters={"project": self.project},
                fields=[
                    "name",
                    "subject",
                    "status",
                    "exp_start_date",
                    "exp_end_date",
                    "description",
                ],
            )

            existing_project_tasks = {task.name: task for task in project_tasks}

            for activity in self.activities:
                if activity.task and activity.task in existing_project_tasks:
                    # Update existing task
                    task = existing_project_tasks[activity.task]
                    frappe.db.set_value(
                        "Task",
                        task.name,
                        {
                            "subject": activity.subject,
                            "status": activity.status,
                            "exp_start_date": activity.start_date,
                            "exp_end_date": activity.end_date,
                            "description": activity.notes,
                        },
                        update_modified=False,
                    )
                elif not activity.task:
                    # Create new task only if it doesn't exist
                    new_task = frappe.get_doc(
                        {
                            "doctype": "Task",
                            "project": self.project,
                            "subject": activity.subject,
                            "status": activity.status,
                            "exp_start_date": activity.start_date,
                            "exp_end_date": activity.end_date,
                            "description": activity.notes,
                        }
                    )
                    new_task.insert()
                    activity.task = new_task.name

            self.save()
            self.reload()
            frappe.db.commit()

            self.show_sync_success_message("Activities synced with tasks successfully.")
            return True
        except Exception as e:
            self.show_sync_error_message("Error syncing activities with tasks", e)
            return False

    @frappe.whitelist()
    def sync_tasks_with_activities(self):
        if not self.project:
            return False

        try:
            project_tasks = frappe.get_all(
                "Task",
                filters={"project": self.project},
                fields=[
                    "name",
                    "subject",
                    "status",
                    "exp_start_date",
                    "exp_end_date",
                    "description",
                ],
            )

            existing_activities = {
                activity.task: activity for activity in self.activities if activity.task
            }

            for task in project_tasks:
                if task.name in existing_activities:
                    # Update existing activity
                    activity = existing_activities[task.name]
                    activity.subject = task.subject
                    activity.status = task.status
                    activity.start_date = task.exp_start_date
                    activity.end_date = task.exp_end_date
                    activity.notes = task.description
                else:
                    # Add new activity for project task
                    self.append(
                        "activities",
                        {
                            "task": task.name,
                            "subject": task.subject,
                            "status": task.status,
                            "start_date": task.exp_start_date,
                            "end_date": task.exp_end_date,
                            "notes": task.description,
                        },
                    )

            self.save()
            self.reload()
            frappe.db.commit()

            self.show_sync_success_message("Tasks synced with activities successfully.")
            return True
        except Exception as e:
            self.show_sync_error_message("Error syncing tasks with activities", e)
            return False

    def sync_product_features_with_tasks(self):
        if not self.project:
            return False

        try:
            project_tasks = frappe.get_all(
                "Task", filters={"project": self.project}, fields=["name"]
            )
            project_task_names = {task.name for task in project_tasks}

            for feature in self.product_features:
                if feature.task_link and feature.task_link not in project_task_names:
                    feature.task_link = None
                elif not feature.task_link:
                    new_task = frappe.get_doc(
                        {
                            "doctype": "Task",
                            "project": self.project,
                            "subject": feature.feature_name,
                            "description": feature.description,
                            "status": "Open",
                        }
                    )
                    new_task.insert()
                    feature.task_link = new_task.name

            # No need to call self.save() here as this method is called during validation
            return True
        except Exception as e:
            self.show_sync_error_message("Error syncing product features with tasks", e)
            return False

    def show_sync_success_message(self, message):
        frappe.publish_realtime(
            "show_alert",
            {"message": _(message), "indicator": "green"},
            user=frappe.session.user,
        )

    def show_sync_error_message(self, message, exception):
        frappe.log_error(
            f"{message}: {str(exception)}", "Product Requirements Sync Error"
        )
        frappe.publish_realtime(
            "show_alert",
            {
                "message": _(f"{message}. Check error log for details."),
                "indicator": "red",
            },
            user=frappe.session.user,
        )
