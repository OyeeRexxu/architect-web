from django.core.management.base import BaseCommand
from main.models import (
    Testimonial, SoftwareTool, WhyChooseUsItem, CommitmentItem, 
    ProcessStep, AboutGalleryImage, SiteSettings, HomePage, AboutPage, ContactPage
)

class Command(BaseCommand):
    help = 'Populates the database with initial data from hardcoded templates'

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating initial data...")

        # 1. Site Settings (Singleton)
        settings = SiteSettings.load()
        settings.site_name = "ConstructPro"
        settings.address = "1234 Builder Lane, Architect City, AC 54321"
        settings.phone_number = "+1 123 456 7895"
        settings.email = "info@constructorpro.com"
        settings.save()
        self.stdout.write("Site Settings updated.")

        # 2. Testimonials
        Testimonial.objects.all().delete()
        testimonials_data = [
            {
                "name": "Emily", "role": "Customer", "rating": 5, "order": 1,
                "content": "When we first met the team we knew we had found what we needed a group of highly experienced, sensitive designers and technicians."
            },
            {
                "name": "Adam", "role": "Customer", "rating": 5, "order": 2,
                "content": "I just wanted to take a moment to send a special thank you for the work you done to provide us with the countertop estimation take out with this type of project."
            },
            {
                "name": "Michael", "role": "Customer", "rating": 5, "order": 3,
                "content": "Outstanding work! The team delivered exactly what we needed on time and within budget. Highly professional and creative approach to our project."
            }
        ]
        for data in testimonials_data:
            Testimonial.objects.create(**data)
        self.stdout.write(f"Created {len(testimonials_data)} testimonials.")

        # 3. Why Choose Us Items
        WhyChooseUsItem.objects.all().delete()
        wcu_data = [
            {
                "title": "Highly Accurate Take-offs",
                "description": "Precision-driven quantity take-offs ensuring error-free estimates every time.",
                "icon_svg": '<svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor"><path d="M9,20.42L2.79,14.21L5.62,11.38L9,14.77L18.88,4.88L21.71,7.71L9,20.42Z" /></svg>',
                "order": 1
            },
            {
                "title": "Fast Turnaround Time",
                "description": "Quick delivery without compromising on quality or accuracy.",
                "icon_svg": '<svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor"><path d="M12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22C6.47,22 2,17.5 2,12A10,10 0 0,1 12,2M12.5,7V12.25L17,14.92L16.25,16.15L11,13V7H12.5Z" /></svg>',
                "order": 2
            },
            {
                "title": "Cost-Effective Pricing",
                "description": "Competitive offshore pricing that maximizes your project budget.",
                "icon_svg": '<svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor"><path d="M7,15H9C9,16.08 10.37,17 12,17C13.63,17 15,16.08 15,15C15,13.9 13.96,13.5 11.76,12.97C9.64,12.44 7,11.78 7,9C7,7.21 8.47,5.69 10.5,5.18V3H13.5V5.18C15.53,5.69 17,7.21 17,9H15C15,7.92 13.63,7 12,7C10.37,7 9,7.92 9,9C9,10.1 10.04,10.5 12.24,11.03C14.36,11.56 17,12.22 17,15C17,16.79 15.53,18.31 13.5,18.82V21H10.5V18.82C8.47,18.31 7,16.79 7,15Z" /></svg>',
                "order": 3
            },
            {
                "title": "Experienced Team",
                "description": "Skilled estimators and engineers with industry expertise.",
                "icon_svg": '<svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor"><path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4M11,17V16H9V14H13V13H10A1,1 0 0,1 9,12V9A1,1 0 0,1 10,8H11V7H13V8H15V10H11V11H14A1,1 0 0,1 15,12V15A1,1 0 0,1 14,16H13V17H11Z" /></svg>',
                "order": 4
            },
            {
                "title": "Industry-Standard Software",
                "description": "Utilizing the latest tools for maximum precision and efficiency.",
                "icon_svg": '<svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor"><path d="M21,16.5C21,16.88 20.79,17.21 20.47,17.38L12.57,21.82C12.41,21.94 12.21,22 12,22C11.79,22 11.59,21.94 11.43,21.82L3.53,17.38C3.21,17.21 3,16.88 3,16.5V7.5C3,7.12 3.21,6.79 3.53,6.62L11.43,2.18C11.59,2.06 11.79,2 12,2C12.21,2 12.41,2.06 12.57,2.18L20.47,6.62C20.79,6.79 21,7.12 21,7.5V16.5M12,4.15L5,8.09V15.91L12,19.85L19,15.91V8.09L12,4.15Z" /></svg>',
                "order": 5
            },
            {
                "title": "Secure Data Handling",
                "description": "Confidential and secure management of all your project data.",
                "icon_svg": '<svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor"><path d="M12,1L3,5V11C3,16.55 6.84,21.74 12,23C17.16,21.74 21,16.55 21,11V5L12,1M12,5A3,3 0 0,1 15,8A3,3 0 0,1 12,11A3,3 0 0,1 9,8A3,3 0 0,1 12,5M17.13,17C15.92,18.85 14.11,20.24 12,20.92C9.89,20.24 8.08,18.85 6.87,17C6.53,16.5 6.24,16 6,15.47C6,13.82 8.71,12.47 12,12.47C15.29,12.47 18,13.79 18,15.47C17.76,16 17.47,16.5 17.13,17Z" /></svg>',
                "order": 6
            }
        ]
        for data in wcu_data:
            WhyChooseUsItem.objects.create(**data)
        self.stdout.write(f"Created {len(wcu_data)} Why Choose Us items.")

        # 4. Commitment Items
        CommitmentItem.objects.all().delete()
        commit_data = [
            {"title": "100% Accuracy & Quality Assurance", "description": "Every deliverable undergoes rigorous quality checks to ensure absolute accuracy.", "number": "01", "order": 1},
            {"title": "On-Time Delivery", "description": "We respect your deadlines and ensure timely completion of all projects.", "number": "02", "order": 2},
            {"title": "Clear Communication", "description": "Transparent and continuous communication throughout the project lifecycle.", "number": "03", "order": 3},
            {"title": "Long-Term Partnership", "description": "We build lasting relationships, becoming an extension of your team.", "number": "04", "order": 4},
        ]
        for data in commit_data:
            CommitmentItem.objects.create(**data)
        self.stdout.write(f"Created {len(commit_data)} Commitment items.")

        # 5. Process Steps
        ProcessStep.objects.all().delete()
        process_data = [
            {"title": "Planning Stage", "description": "First we understand the need and plan the project accordingly.", "number": "01", "order": 1, "icon_svg": '<svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor"><path d="M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3M7,7H17V5H19V19H5V5H7V7M17,11H7V9H17V11M15,15H7V13H15V15Z"/></svg>'},
            {"title": "Design Process", "description": "Discussed with the design team and start designing work.", "number": "02", "order": 2, "icon_svg": '<svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor"><path d="M21.71,5.29L18.71,2.29C18.32,1.9 17.69,1.9 17.3,2.29L14.29,5.29C13.9,5.68 13.9,6.32 14.29,6.71L17.29,9.71C17.68,10.1 18.32,10.1 18.71,9.71L21.71,6.71C22.1,6.32 22.1,5.68 21.71,5.29M17,14.25V13C17,12.45 16.55,12 16,12C15.45,12 15,12.45 15,13V15C15,15.55 15.45,16 16,16H18C18.55,16 19,15.55 19,15C19,14.45 18.55,14 18,14H17.79L19.92,11.87L18.5,10.45L17,14.25M12,2C11.45,2 11,2.45 11,3V5C11,5.55 11.45,6 12,6C12.55,6 13,5.55 13,5V3C13,2.45 12.55,2 12,2M4.5,10.5V13.5C4.5,13.78 4.72,14 5,14H8C8.28,14 8.5,13.78 8.5,13.5V10.5C8.5,10.22 8.28,10 8,10H5C4.72,10 4.5,10.22 4.5,10.5M20,20C20,21.1 19.1,22 18,22H6C4.9,22 4,21.1 4,20V8C4,6.9 4.9,6 6,6H9C9,7.66 10.34,9 12,9C13.66,9 15,7.66 15,6H18C19.1,6 20,6.9 20,8V20Z"/></svg>'},
            {"title": "Execution Phase", "description": "Give the client wireframe to execute the same according to the approval.", "number": "03", "order": 3, "icon_svg": '<svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor"><path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4M12,6A6,6 0 0,0 6,12A6,6 0 0,0 12,18A6,6 0 0,0 18,12A6,6 0 0,0 12,6M12,8A4,4 0 0,1 16,12A4,4 0 0,1 12,16A4,4 0 0,1 8,12A4,4 0 0,1 12,8Z"/></svg>'},
            {"title": "Completed Projects", "description": "After approval, get the final phase and touch as per client feedback.", "number": "04", "order": 4, "icon_svg": '<svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor"><path d="M12,3L2,12H5V20H19V12H22L12,3M12,8.75A2.25,2.25 0 0,1 14.25,11A2.25,2.25 0 0,1 12,13.25A2.25,2.25 0 0,1 9.75,11A2.25,2.25 0 0,1 12,8.75M12,15C13.5,15 16.5,15.75 16.5,17.25V18H7.5V17.25C7.5,15.75 10.5,15 12,15Z"/></svg>'},
        ]
        for data in process_data:
            ProcessStep.objects.create(**data)
        self.stdout.write(f"Created {len(process_data)} Process steps.")

        # 6. Software Tools
        SoftwareTool.objects.all().delete()
        tools = ["autodesk autocad", "Revit", "sketchUP", "alphacam", "bluebeam", 
                 "mastercam", "mozaik", "design 2020", "inventor cam", "Capture"]
        for i, name in enumerate(tools):
            SoftwareTool.objects.create(name=name, image=f"images/software/{name}.png", order=i+1)
        self.stdout.write(f"Created {len(tools)} Software tools.")
        
        # 7. About Gallery Images
        AboutGalleryImage.objects.all().delete()
        gallery = [
            ("Tech", "images/generated/blueprint.png"),
            ("Build", "images/generated/facade.png"),
            ("Design", "images/generated/detail.png"),
            ("Global", "images/generated/global.png"),
            ("Team", "images/generated/team.png")
        ]
        for i, (title, path) in enumerate(gallery):
            AboutGalleryImage.objects.create(title=title, image=path, order=i+1)
        self.stdout.write(f"Created {len(gallery)} About Gallery images.")

        self.stdout.write(self.style.SUCCESS('Successfully populated initial data.'))
