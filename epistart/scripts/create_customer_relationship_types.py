import frappe


def create_customer_relationship_types():
    relationship_types = [
        {
            "relationship_type": "Personal Assistance",
            "description": "Direct interaction between customer and company representative, either during the sales process, after the sale, or both.",
            "examples": "In-store sales staff, call center support, email support for complex products.",
        },
        {
            "relationship_type": "Dedicated Personal Assistance",
            "description": "A company representative is assigned specifically to an individual client. This is the deepest and most intimate type of relationship.",
            "examples": "Private banking services, personal shoppers in luxury retail, account managers for large B2B clients.",
        },
        {
            "relationship_type": "Self-Service",
            "description": "The company provides all necessary means for customers to help themselves, with no direct relationship with the company.",
            "examples": "Self-checkout at supermarkets, online FAQ sections, product manuals for self-assembly furniture.",
        },
        {
            "relationship_type": "Automated Services",
            "description": "A more sophisticated form of self-service, utilizing automated processes and potentially AI to recognize and serve individual customers.",
            "examples": "Online product recommendations, personalized email marketing campaigns, chatbots for customer service.",
        },
        {
            "relationship_type": "Communities",
            "description": "Companies facilitate connections between community members, often to help customers solve each other's problems.",
            "examples": "User forums for troubleshooting product issues, social media brand communities, fitness app user groups.",
        },
        {
            "relationship_type": "Co-creation",
            "description": "Companies involve customers in the creation or design of new products or content, creating value together.",
            "examples": "YouTube's content creation platform, LEGO Ideas for new set designs, open-source software projects.",
        },
        {
            "relationship_type": "Subscription",
            "description": "Customers pay a recurring fee to access a product or service, creating an ongoing relationship.",
            "examples": "Streaming services like Netflix, software-as-a-service products, subscription box services.",
        },
        {
            "relationship_type": "Transactional",
            "description": "Limited ongoing relationship, focused on individual transactions as needed by the customer.",
            "examples": "One-time purchases at retail stores, occasional service providers like plumbers or electricians.",
        },
        {
            "relationship_type": "Freemium",
            "description": "Basic services are provided for free, with premium features available for a fee, nurturing potential paying customers.",
            "examples": "Spotify's free and premium tiers, LinkedIn's basic and premium accounts, mobile games with in-app purchases.",
        },
        {
            "relationship_type": "Educational",
            "description": "The company provides educational resources to customers, enhancing their ability to use products or services effectively.",
            "examples": "Apple's in-store workshops, HubSpot Academy for marketing education, cooking classes by kitchen appliance manufacturers.",
        },
    ]

    for rel_type in relationship_types:
        if not frappe.db.exists(
            "Customer Relationship Type", rel_type["relationship_type"]
        ):
            doc = frappe.get_doc(
                {
                    "doctype": "Customer Relationship Type",
                    "relationship_type": rel_type["relationship_type"],
                    "description": rel_type["description"],
                    "examples": rel_type["examples"],
                }
            )
            doc.insert()
        else:
            doc = frappe.get_doc(
                "Customer Relationship Type", rel_type["relationship_type"]
            )
            doc.description = rel_type["description"]
            doc.examples = rel_type["examples"]
            doc.save()

    print("Customer Relationship Types have been created or updated.")


# This function can be run to create or update the Customer Relationship Types
create_customer_relationship_types()
