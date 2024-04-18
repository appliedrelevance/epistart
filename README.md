## EpiStart - Lean Startup Methodology for Frappe

EpiStart is an open-source app designed to bring agile project management tools to the Frappe framework. It provides a set of doctypes that allow teams to manage their projects using the Lean Startup methodology. EpiStart is perfect for startups and teams looking to implement agile practices in their Frappe-based applications.

### Installation
To install EpiStart on your Frappe site, follow these steps:

1. Open your terminal and navigate to your Frappe bench folder.
2. Execute the following command to get the app:
   ```
   bench get-app epistart https://github.com/appliedrelevance/epistart.git
   ```
3. Install EpiStart on your site:
   ```
   bench --site your-site-name install-app epistart
   ```

### Doctypes

#### Epic
- **Description:** Represents a large body of work that can be broken down into smaller user stories.
- **Usage:** Use this doctype to group related user stories and track their overall progress.

#### Lean Canvas
- **Description:** A one-page business plan template that helps you deconstruct your idea into its key assumptions.
- **Usage:** Use this doctype to quickly iterate on your business model and keep your team aligned with the startup's vision.

#### Persona
- **Description:** Represents a fictional character that embodies a key user segment for your product.
- **Usage:** Use this doctype to capture important details about your target user segments, including their goals, challenges, and motivations.

#### User Story
- **Description:** Describes a feature from the perspective of the end user, capturing what they want and why.
- **Usage:** Use this doctype to break down features into manageable pieces of work, each with clear acceptance criteria.

### Contributing
Contributions are welcome! If you'd like to contribute to EpiStart, please fork the repository, make your changes, and submit a pull request.

### More Information
For more information on the Lean Startup methodology and agile project management, visit the following sites:
- [The Lean Startup](http://theleanstartup.com/)
- [Agile Methodology](https://www.agilealliance.org/agile101/)
