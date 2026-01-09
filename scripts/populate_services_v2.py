from main.models import Service, ServiceSection, ServiceFeature, ServiceImage

def populate():
    data = [
        {
            "title": "Estimation & Quantity Take-Off Services",
            "subtitle": "Accurate and detailed cost estimation for your construction projects.",
            "overview": "We provide accurate, detailed, and cost-effective Construction Estimation & Quantity Take-Off Services to contractors, builders, developers, and consultants across the globe. By outsourcing your estimating work to us in India, you save time, reduce overhead costs, and improve bidding accuracy.",
            "icon": "fa-solid fa-calculator",
            "image": "services/estimation.png",
            "sections": [
                {
                    "type": "text",
                    "heading": "Note",
                    "content": "Whether you bid on 2 projects per month or 50, we scale our services as per your needs."
                },
                {
                    "type": "tags",
                    "heading": "Who Can Benefit?",
                    "items": [
                        "General Contractors", "Subcontractors", "Builders & Developers", 
                        "Architects & Engineers", "Construction Consultants"
                    ]
                }
            ],
            "features": [
                ("Countertop & Cabinet", "fa-solid fa-layer-group"),
                ("Flooring & Walls", "fa-solid fa-border-all"),
                ("Stone & Tile", "fa-solid fa-shapes"),
                ("Door & Window", "fa-solid fa-door-open"),
                ("Plumbing Fixture", "fa-solid fa-faucet"),
                ("Electrical & Lighting", "fa-regular fa-lightbulb"),
                ("Paint", "fa-solid fa-paint-roller"),
                ("Roofing & Siding", "fa-solid fa-house-chimney"),
                ("Appliances", "fa-solid fa-blender"),
                ("Shower and Tub", "fa-solid fa-bath"),
                ("Door Hardware", "fa-solid fa-key"),
                ("Blinds", "fa-solid fa-align-justify")
            ]
        },
        {
            "title": "Cabinetry, Tops & Millwork Solutions",
            "subtitle": "End-to-end drafting and design solutions for fabricators.",
            "overview": "We provide end-to-end Cabinetry, Countertop (Tops), and Millwork Drafting & Design Solutions to support fabricators and suppliers across the USA and Europe. Our outsourcing services are designed to streamline production, reduce errors, and ensure smooth coordination between design and fabrication. With deep industry understanding, we help you convert concepts, sketches, and specifications into precise, shop-ready drawings and 3D models.",
            "icon": "fa-solid fa-cabinet-filing",
            "image": "services/cabinetry.png",
            "sections": [
                {
                    "type": "benefits",
                    "heading": "Why Fabricators & Suppliers Choose Us",
                    "items": [
                        "Specialized Support for USA & European Markets",
                        "Fabrication-Ready Drawings with High Accuracy",
                        "Reduced Rework & Production Errors",
                        "Fast Turnaround & Scalable Outsourcing",
                        "Cost-Effective Offshore Support",
                        "Confidentiality & Secure Data Handling"
                    ]
                },
                {
                    "type": "tags",
                    "heading": "Who We Support",
                    "items": [
                        "Cabinet Fabricators", "Millwork Manufacturers", "Countertop Fabricators",
                        "Kitchen & Bath Suppliers", "Interior Fit-Out Companies", 
                        "Commercial & Residential Project Suppliers"
                    ]
                }
            ],
            "features": [
                ("Design 2020, Cabinet Vision & Mozaik", "fa-solid fa-pen-ruler"),
                ("Countertop & Cabinet Shop Drawing", "fa-solid fa-file-invoice"),
                ("Stone Slab Nesting/Layout Support", "fa-solid fa-cubes"),
                ("LT-55 software Template Files Support", "fa-solid fa-file-code"),
                ("Fabrication-Ready Layouts", "fa-solid fa-industry"),
                ("CNC-Ready Drawings", "fa-solid fa-memory"),
                ("Stone Profit System - Quote Preparation", "fa-solid fa-file-invoice-dollar"),
                ("Moraware & StoneApp", "fa-solid fa-calculator")
            ]
        },
        {
            "title": "2D & 3D CAD Drafting Outsourcing Services",
            "subtitle": "Reliable and cost-effective drafting for global construction.",
            "overview": "We offer reliable and cost-effective 2D & 3D CAD Drafting Outsourcing Services to support architects, engineers, contractors, and manufacturing companies worldwide. By outsourcing your CAD drafting needs to us, you gain high-quality drawings, faster turnaround, and reduced operational costs without compromising accuracy.",
            "icon": "fa-solid fa-pen-to-square",
            "image": "services/cad.png",
            "sections": [
                {
                    "type": "benefits",
                    "heading": "Why Outsource CAD Drafting to Us?",
                    "items": [
                        "Significant Cost Savings", "High Accuracy & Quality Control",
                        "Quick Turnaround Time", "Scalable Team Support",
                        "Strict Confidentiality & Data Security", "Easy Communication & Time-Zone Flexibility"
                    ]
                },
                {
                    "type": "tags",
                    "heading": "Industries We Support",
                    "items": [
                        "Architecture & Construction Firms", "Engineering & Manufacturing Companies",
                        "Interior Design Studios", "Real Estate Developers",
                        "Product Design & Fabrication Firms", "Contractors & Consultants"
                    ]
                }
            ],
            "features": [
                ("Architectural Floor Plans", "fa-solid fa-building"),
                ("Construction & Permit Drawings", "fa-solid fa-file-signature"),
                ("MEP Drafting", "fa-solid fa-bolt"),
                ("Shop & As-Built Drawings", "fa-solid fa-clipboard-check"),
                ("PDF to AutoCAD Conversion", "fa-solid fa-file-pdf"),
                ("3D Architectural Models", "fa-solid fa-cube"),
                ("Mechanical Parts Modeling", "fa-solid fa-gears"),
                ("Product 3D Models", "fa-solid fa-box-open"),
                ("3D Visualization", "fa-solid fa-eye"),
                ("Concept Models", "fa-solid fa-lightbulb")
            ]
        },
        {
            "title": "CNC Programming Support",
            "subtitle": "Professional CNC programming for countertops fabrication.",
            "overview": "We provide professional CNC programming support for companies in the countertops industry. Whether you work with granite, marble, quartz, or other materials, our experts create precise and optimized CNC programs tailored to your designs.",
            "icon": "fa-solid fa-microchip",
            "image": "services/cnc.png",
            "sections": [
                {
                    "type": "benefits",
                    "heading": "Why Choose Us",
                    "items": [
                        "Expertise: Years of experience in CNC programming for countertops",
                        "Accuracy: Programs optimized for minimal waste and maximum efficiency",
                        "Flexible Outsourcing: Scale your production without hiring extra staff",
                        "Fast Turnaround: Get your programs when you need them",
                        "Cost-Effective: Reduce overhead and production downtime"
                    ]
                },
                {
                    "type": "process",
                    "heading": "How It Works",
                    "items": [
                        "Send Your Designs: Upload your CAD files or drawings",
                        "We Program: Our team creates precise CNC programs",
                        "Receive & Produce: Download ready-to-run programs and start production immediately"
                    ]
                }
            ],
            "features": [
                ("Countertop Programming", "fa-solid fa-code"),
                ("Countertop Toolpaths", "fa-solid fa-route"),
                ("AlphaCAM Software", "fa-solid fa-compact-disc"),
                ("Slabsmith Software", "fa-solid fa-layer-group")
            ]
        },
        {
            "title": "Architecture, Interior & Structural Design",
            "subtitle": "Transforming vision into reality with comprehensive design services.",
            "overview": "We specialize in transforming your vision into reality with our comprehensive architecture, interior, and structural design services. Whether it’s a residential project, commercial space, or industrial building, our expert team ensures innovative, functional, and sustainable designs that exceed expectations.",
            "icon": "fa-solid fa-compass-drafting",
            "image": "services/architecture.png",
            "sections": [
                {
                    "type": "benefits",
                    "heading": "Why Choose Us",
                    "items": [
                        "Experienced Team of Architects, Interior Designers, and Structural Engineers",
                        "Innovative & Client-Centric Designs",
                        "Focus on Sustainability & Safety",
                        "Timely Delivery & Budget-Friendly Solutions"
                    ]
                },
                {
                    "type": "process",
                    "heading": "Our Process",
                    "items": [
                        "Consultation – Understand your needs, preferences, and project goals.",
                        "Design & Planning – Creative conceptual designs with detailed planning.",
                        "Execution & Oversight – Structural and interior planning to ensure flawless execution.",
                        "Delivery & Support – On-time delivery with ongoing support for modifications."
                    ]
                }
            ],
            "features": [
                ("Conceptual Design & Planning", "fa-regular fa-paper-plane"),
                ("3D Modeling & Visualization", "fa-solid fa-cube"),
                ("Building Layout", "fa-solid fa-ruler-combined"),
                ("Sustainable Solutions", "fa-solid fa-leaf"),
                ("Residential & Commercial Interiors", "fa-solid fa-couch"),
                ("Space Optimization", "fa-solid fa-arrows-to-dot"),
                ("Customized Designs", "fa-solid fa-palette"),
                ("Material Selection", "fa-solid fa-swatchbook"),
                ("Structural Analysis", "fa-solid fa-building-shield"),
                ("Building Safety", "fa-solid fa-helmet-safety"),
                ("Concrete, Steel & Timber", "fa-solid fa-cubes-stacked"),
                ("Cost-Effective Solutions", "fa-solid fa-piggy-bank")
            ]
        },
        {
            "title": "Data Entry Services",
            "subtitle": "Fast, accurate, and reliable data management solutions.",
            "overview": "We provide fast, accurate, and reliable data entry services to help businesses manage, organize, and utilize their data efficiently. Our experienced team ensures high-quality results while maintaining strict confidentiality.",
            "icon": "fa-solid fa-keyboard",
            "image": "services/data_entry.png",
            "sections": [
                {
                    "type": "benefits",
                    "heading": "Why Choose Us",
                    "items": [
                        "Experienced Team of Data Entry Specialists",
                        "High Accuracy & Attention to Detail",
                        "Fast Turnaround Time & Timely Delivery",
                        "Confidentiality & Data Security Guaranteed",
                        "Cost-Effective Outsourcing Solutions"
                    ]
                },
                {
                    "type": "process",
                    "heading": "Our Process",
                    "items": [
                        "Understanding Your Requirements – We start by analyzing your data needs.",
                        "Data Collection & Entry – Efficient and accurate input of all your information.",
                        "Quality Check – Thorough verification to ensure 100% accuracy.",
                        "Delivery & Support – Timely submission and ongoing support for any modifications."
                    ]
                }
            ],
            "features": [
                ("Manual Data", "fa-solid fa-hand-holding"),
                ("Data Processing", "fa-solid fa-server"),
                ("Database Management", "fa-solid fa-database"),
                ("Online & Offline Data Entry", "fa-solid fa-wifi"),
                ("Data Conversion", "fa-solid fa-file-export")
            ]
        }
    ]

    for idx, item in enumerate(data):
        print(f"Processing: {item['title']}...")
        
        service, created = Service.objects.update_or_create(
            title=item['title'],
            defaults={
                'subtitle': item['subtitle'],
                'overview': item['overview'],
                'icon': item['icon'],
                'image': item['image'],
                'order': idx + 1
            }
        )

        service.sections.all().delete()
        service.features.all().delete()

        for s_idx, section in enumerate(item['sections']):
            items_text = "\n".join(section.get('items', []))
            ServiceSection.objects.create(
                service=service,
                heading=section['heading'],
                section_type=section['type'],
                content=section.get('content', ''),
                items=items_text,
                order=s_idx + 1
            )

        for f_idx, (feat_title, feat_icon) in enumerate(item['features']):
            ServiceFeature.objects.create(
                service=service,
                title=feat_title,
                icon=feat_icon,
                order=f_idx + 1
            )
        
        if service.images.count() == 0:
            for i in range(12):
                 ServiceImage.objects.create(service=service, image=item['image'], caption=f"{item['title']} Example {i+1}", order=i)

    print("Success! All services populated.")

populate()
