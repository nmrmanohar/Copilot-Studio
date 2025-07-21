import os, json, zipfile, csv

# Define case studies with their sample contents
case_studies = [
    {
        "name": "healthcare-copilot-solution",
        "files": {
            "README.md": "# Healthcare Patient-Care Coordination Copilot\n\nThis package contains sample data and environment setup scripts for the Healthcare Patient-Care Coordination Copilot solution described in the case study.\n",
            "SampleData/patientList.json": json.dumps([
                {"id": "patient-001", "name": "Jane Doe", "dob": "1985-02-14", "contact": "jane.doe@example.com"},
                {"id": "patient-002", "name": "John Smith", "dob": "1979-08-30", "contact": "john.smith@example.com"}
            ], indent=2),
            "SampleData/appointments.csv": "appointmentId,patientId,date\napt-001,patient-001,2025-08-01\napt-002,patient-002,2025-08-02\n",
            "scripts/setup-env.ps1": "Write-Host 'Placeholder script to configure environment variables'"
        }
    },
    {
        "name": "retail-copilot-solution",
        "files": {
            "README.md": "# Retail Omnichannel Customer Service & Returns Copilot\n\nSample data and connector setup for the Retail Copilot.\n",
            "SampleData/orders.csv": "orderId,customerEmail,status,total\n1001,alice@example.com,Shipped,89.99\n1002,bob@example.com,Delivered,39.99\n",
            "SampleData/products.csv": "productId,name,category\nSKU123,Running Shoes,Footwear\nSKU124,T-Shirt,Apparel\n",
            "scripts/configure-connectors.ps1": "Write-Host 'Placeholder script to configure Shopify and Loyalty connectors'"
        }
    },
    {
        "name": "smartfactory-copilot-solution",
        "files": {
            "README.md": "# Manufacturing Smart-Factory Operations Copilot\n\nSample IoT telemetry and deployment script.\n",
            "SampleData/telemetry.json": json.dumps([
                {"assetId": "machine-A1", "timestamp": "2025-07-20T08:00:00Z", "vibration": 3.7},
                {"assetId": "machine-B2", "timestamp": "2025-07-20T08:05:00Z", "vibration": 7.4}
            ], indent=2),
            "scripts/deploy-flows.ps1": "Write-Host 'Placeholder script to publish maintenance flows'"
        }
    },
    {
        "name": "finance-compliance-copilot",
        "files": {
            "README.md": "# Financial Services Risk & Compliance Copilot\n\nSample profiles and transactions for AML screening demo.\n",
            "SampleData/customerProfiles.json": json.dumps([
                {"customerId": "CUST001", "name": "Alice Smith", "country": "US"},
                {"customerId": "CUST002", "name": "Bob Lee", "country": "GB"}
            ], indent=2),
            "SampleData/transactions.csv": "transactionId,customerId,amount,currency,date\nTXN1001,CUST001,12000,USD,2025-07-19\nTXN1002,CUST002,500,GBP,2025-07-19\n",
            "templates/SAR-Template.docx": "PLACEHOLDER DOCX CONTENT"
        }
    },
    {
        "name": "logistics-copilot-solution",
        "files": {
            "README.md": "# Logistics Supply-Chain Fulfilment & Route Optimisation Copilot\n\nSample telematics data, orders, and deployment script.\n",
            "SampleData/telematics.json": json.dumps([
                {"truckId": "TX-1001", "timestamp": "2025-07-20T09:00:00Z", "latitude": 47.608013, "longitude": -122.335167, "temperature": 4.5}
            ], indent=2),
            "SampleData/orders.csv": "orderId,origin,destination,status\nORD001,Seattle,Portland,In Transit\nORD002,LA,San Diego,Delayed\n",
            "scripts/deploy-logistics-connectors.ps1": "Write-Host 'Placeholder script to configure Bing Maps and MQTT connectors'"
        }
    }
]

# Create zip files
created_files = []
for cs in case_studies:
    zip_name = cs['name'] + '.zip'
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for path, content in cs['files'].items():
            # Ensure directory exists in zip path
            zf.writestr(path, content)
    created_files.append(zip_name)

print("Created zip files:")
for f in created_files:
    print(f"- {f}")