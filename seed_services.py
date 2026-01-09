
import os
import sys
import django

# Add current directory to path
sys.path.append(os.getcwd())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "construct_site.settings")
django.setup()

from main.models import Service, ServiceSection

# Clear existing data to avoid duplicates during dev
Service.objects.all().delete()

services_data = [
    {
        "title": "Estimation & Quantity Take-Off Services",
        "overview": "We provide accurate, detailed, and cost-effective Construction Estimation & Quantity Take-Off Services to contractors, builders, developers, and consultants across the globe. By outsourcing your estimating work to us in India, you save time, reduce overhead costs, and improve bidding accuracy.",
        "icon": "calculator",
        "image": "services/estimation.png",
        "gallery": [
            {"image": "services/estimation.png", "caption": "Estimation Take-Off"}
        ],
        "sections": [
            {
                "heading": "Who Can Benefit?",
                "type": "tags",
                "items": "General Contractors\nSubcontractors\nBuilders & Developers\nArchitects & Engineers\nConstruction Consultants",
                "is_subsection": True
            },
            {
                "heading": "Note",
                "type": "text",
                "content": "Whether you bid on 2 projects per month or 50, we scale our services as per your needs.",
                "is_subsection": True
            },
            {
                "heading": "Our Estimation Services Include",
                "type": "list",
                "items": "Countertop & Cabinet\nFlooring & Walls\nStone & Tile\nDoor & Window\nPlumbing Fixture\nElectrical & Lighting\nPaint\nRoofing & Siding\nAppliances\nShower and Tub\nDoor Hardware\nBlinds"
            }
        ]
    },

    {
        "title": "Cabinetry, Tops & Millwork Solutions",
        "overview": "We provide end-to-end Cabinetry, Countertop (Tops), and Millwork Drafting & Design Solutions to support fabricators and suppliers across the USA and Europe. Our outsourcing services are designed to streamline production, reduce errors, and ensure smooth coordination between design and fabrication. With deep industry understanding, we help you convert concepts, sketches, and specifications into precise, shop-ready drawings and 3D models.",
        "icon": "cabinet",
        "image": "services/cabinetry.png",

        "gallery": [
            {"image": "project_kitchen_cabinetry.png", "caption": "Modern Kitchen Cabinetry"}
        ],
        "sections": [
            {
                "heading": "Our Cabinetry, Top & Millwork Services",
                "type": "list",
                "items": "Design 2020, Cabinet Vision & Mozaik\nCountertop & Cabinet Shop Drawing\nStone Slab Nesting/Layout Support\nLT-55 software Template Files Support\nFabrication-Ready Layouts\nCNC-Ready Drawings\nStone Profit System - Quote Preparation\nMoraware & StoneApp – Quote Preparation"
            },
            {
                "heading": "Why Fabricators & Suppliers Choose Us",
                "type": "benefits",
                "items": "Specialized Support for USA & European Markets\nFabrication-Ready Drawings with High Accuracy\nReduced Rework & Production Errors\nFast Turnaround & Scalable Outsourcing\nCost-Effective Offshore Support\nConfidentiality & Secure Data Handling"
            },
            {
                "heading": "Who We Support",
                "type": "tags",
                "items": "Cabinet Fabricators\nMillwork Manufacturers\nCountertop Fabricators\nKitchen & Bath Suppliers\nInterior Fit-Out Companies\nCommercial & Residential Project Suppliers"
            }
        ]
    },
    {
        "title": "2D & 3D CAD Drafting Outsourcing Services",
        "overview": "We offer reliable and cost-effective 2D & 3D CAD Drafting Outsourcing Services to support architects, engineers, contractors, and manufacturing companies worldwide. By outsourcing your CAD drafting needs to us, you gain high-quality drawings, faster turnaround, and reduced operational costs without compromising accuracy.",
        "icon": "cad",
        "image": "services/cad.png",

        "gallery": [
             {"image": "project_commercial_complex.png", "caption": "Commercial Complex Drafting"},
             {"image": "project_modern_residence.png", "caption": "Residential Layouts"}
        ],
        "sections": [
            {
                "heading": "Our Outsourced CAD Drafting Services",
                "type": "list",
                "items": "Architectural Floor Plans, Elevations & Sections\nConstruction & Permit Drawings\nMechanical, Electrical & Plumbing (MEP) Drafting\nShop Drawings & As-Built Drawings\nPDF / Hand Sketch to AutoCAD Conversion\n3D Architectural & Structural Models\nMechanical Parts & Assembly Modeling\nProduct & Industrial 3D Models\nInterior & Exterior 3D Visualization\nConcept & Presentation Models"
            },
            {
                "heading": "Why Outsource CAD Drafting to Us?",
                "type": "benefits",
                "items": "Significant Cost Savings\nHigh Accuracy & Quality Control\nQuick Turnaround Time\nScalable Team Support\nStrict Confidentiality & Data Security\nEasy Communication & Time-Zone Flexibility"
            },
            {
                "heading": "Industries We Support",
                "type": "tags",
                "items": "Architecture & Construction Firms\nEngineering & Manufacturing Companies\nInterior Design Studios\nReal Estate Developers\nProduct Design & Fabrication Firms\nContractors & Consultants"
            }
        ]
    },
    {
        "title": "CNC Programming Support for Countertops Fabrication",
        "overview": "We provide professional CNC programming support for companies in the countertops industry. Whether you work with granite, marble, quartz, or other materials, our experts create precise and optimized CNC programs tailored to your designs.",
        "icon": "cnc",
        "image": "services/cnc.png",

        "gallery": [],
        "sections": [
            {
                "heading": "Our Services Include",
                "type": "list",
                "items": "Countertop Programming\nCountertop Toolpaths\nAlphaCAM Software\nSlabsmith Software"
            },
            {
                "heading": "Why Choose Us",
                "type": "benefits",
                "items": "Expertise: Years of experience in CNC programming for countertops\nAccuracy: Programs optimized for minimal waste and maximum efficiency\nFlexible Outsourcing: Scale your production without hiring extra staff\nFast Turnaround: Get your programs when you need them\nCost-Effective: Reduce overhead and production downtime"
            },
            {
                "heading": "How It Works",
                "type": "process",
                "items": "Send Your Designs: Upload your CAD files or drawings\nWe Program: Our team creates precise CNC programs\nReceive & Produce: Download ready-to-run programs and start production immediately"
            }
        ]
    },
    {
        "title": "Architecture, Interior & Structural Design Services",
        "overview": "At ConstructPro, we specialize in transforming your vision into reality with our comprehensive architecture, interior, and structural design services. Whether it’s a residential project, commercial space, or industrial building, our expert team ensures innovative, functional, and sustainable designs that exceed expectations.",
        "icon": "architecture",
        "image": "services/architecture.png",

        "gallery": [
            {"image": "project_modern_residence.png", "caption": "Modern Villa Design"},
             {"image": "project_commercial_complex.png", "caption": "Office Tower Concept"}
        ],
        "sections": [
            {
                "heading": "Our Services Include",
                "type": "list",
                "items": "Conceptual Design & Planning\n3D Modeling & Visualization\nBuilding Layout & Space Planning\nSustainable & Green Architecture Solutions\nResidential & Commercial Interiors\nSpace Optimization & Functional Layouts\nModern, Contemporary & Customized Designs\nMaterial Selection & Décor Planning\nStructural Analysis & Planning\nBuilding Safety & Code Compliance\nConcrete, Steel & Timber Structural Designs\nCost-Effective & Efficient Solutions"
            },
            {
                "heading": "Why Choose Us",
                "type": "benefits",
                "items": "Experienced Team of Architects, Interior Designers, and Structural Engineers\nInnovative & Client-Centric Designs\nFocus on Sustainability & Safety\nTimely Delivery & Budget-Friendly Solutions"
            },
            {
                "heading": "Our Process",
                "type": "process",
                "items": "Consultation – Understand your needs, preferences, and project goals.\nDesign & Planning – Creative conceptual designs with detailed planning.\nExecution & Oversight – Structural and interior planning to ensure flawless execution.\nDelivery & Support – On-time delivery with ongoing support for modifications."
            }
        ]
    },
    {
        "title": "Data Entry Services",
        "overview": "At ConstructPro, we provide fast, accurate, and reliable data entry services to help businesses manage, organize, and utilize their data efficiently. Our experienced team ensures high-quality results while maintaining strict confidentiality.",
        "icon": "interior",
        "image": "services/data_entry.png",

        "gallery": [],
        "sections": [
            {
                "heading": "Our Data Entry Services Include",
                "type": "list",
                "items": "Manual Data\nData Processing\nDatabase Management\nOnline & Offline Data Entry\nData Conversion."
            },
            {
                "heading": "Why Choose Us",
                "type": "benefits",
                "items": "Experienced Team of Data Entry Specialists\nHigh Accuracy & Attention to Detail\nFast Turnaround Time & Timely Delivery\nConfidentiality & Data Security Guaranteed\nCost-Effective Outsourcing Solutions"
            },
            {
                "heading": "Our Process",
                "type": "process",
                "items": "Understanding Your Requirements – We start by analyzing your data needs.\nData Collection & Entry – Efficient and accurate input of all your information.\nQuality Check – Thorough verification to ensure 100% accuracy.\nDelivery & Support – Timely submission and ongoing support for any modifications."
            }
        ]
    }
]

print("Starting Seed...")
from main.models import Service, ServiceSection, ServiceSoftware, ServiceImage

for index, s_data in enumerate(services_data):
    s = Service.objects.create(
        title=s_data["title"],
        overview=s_data["overview"],
        icon=s_data["icon"],
        image=s_data.get("image", ""),
        order=index+1
    )
    print(f"Created Service: {s.title}")
    
    # Text Sections
    for sect_index, sect_data in enumerate(s_data["sections"]):
        ServiceSection.objects.create(
            service=s,
            heading=sect_data.get("heading", ""),
            section_type=sect_data.get("type", "text"),
            content=sect_data.get("content", ""),
            items=sect_data.get("items", ""),
            is_subsection=sect_data.get("is_subsection", False),
            order=sect_index+1
        )
        print(f"  - Added Section: {sect_data.get('heading')}")



    # Gallery
    gallery_list = s_data.get("gallery", [])
    for img_idx, img in enumerate(gallery_list):
        ServiceImage.objects.create(
            service=s,
            image=img["image"],
            caption=img.get("caption", ""),
            order=img_idx
        )
    if gallery_list:
        print(f"  - Added {len(gallery_list)} Gallery Images")

print("Done!")
