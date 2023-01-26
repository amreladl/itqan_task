{
    "name": "Product Points",
    "version": "15.0",
    "author": "Amr ElAdl",
    "depends": ["sale_management"],
    "data": [
        # Security
        "security/security.xml",
        "security/ir.model.access.csv",
        # Data
        "data/data.xml",
        # Report
        "report/points_report.xml",
        "report/points_report_template.xml",
        # Views
        "views/product_point_view.xml",
        "views/sale_order_view.xml",
    ],
    "installable": True,
}
