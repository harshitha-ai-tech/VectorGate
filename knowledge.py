KNOWLEDGE_TEXT = """
# Propenq Real Estate ERP Knowledge Base

## Context & Overview
**Propenq** is a unified real estate ERP platform designed to streamline business operations from lead acquisition to financial closure. It integrates CRM, Property Management, Inventory, Finance, and HR into a single cohesive system. This document serves as the ground truth for RAG (Retrieval-Augmented Generation) applications, detailing modules, submodules, navigation paths, and data schemas.

---

## 1. CRM Module (Customer Relationship Management)
**Keywords**: sales, enquiry, customer, lead, pipeline, conversion

### 1.1 Lead Management
**Context**: Use this module to capture initial potential customer interest (enquiries) before they are qualified. It is the entry point for the sales cycle.
**Navigation**: CRM > Lead
**Fields**:
*   **Lead Information**: Lead Code, Expected Revenue, Company (Customer Name), Source, Salesperson, Agent, Rating.
*   **Contact Info**: Salutation, Contact Name (First Name), Email, Mobile, Phone.
*   **Address Info**: Street 1, Street 2, City, Zip, State, Country.
*   **Personal Info**: Gender, Date of Birth.
*   **Status**: Tracks progress (e.g., New, Contacted, Qualified).

### 1.2 Opportunity Management
**Context**: Use this module for qualified leads that have a higher probability of conversion. It tracks the specific property interest and negotiation stage.
**Navigation**: CRM > Opportunity
**Fields**:
*   **Main Info**: Name, Salesperson, Email, Expected Revenue, Mobile, Phone, Source, Industry.
*   **Classification**: Project Name, Property Type (Apartment/Commercial/Plot), Agent, Funding Type, Campaign, Rating.
*   **Engagement**: Call Suggestion, Call Summary.
*   **Address**: Street 1, Street 2, Zip, City, State, Country.

### 1.3 Campaign Management
**Context**: Use this module to plan and track marketing initiatives designed to generate leads.
**Navigation**: CRM > Campaign
**Fields**:
*   **Campaign Info**: Code, Name, Status, Start Date, End Date.
*   **Financials**: Budgeted Cost, Actual Cost, Expected Revenue.

### 1.4 Agent Management
**Context**: Use this module to manage external real estate agents or brokers who bring in business for a commission.
**Navigation**: CRM > Agent
**Fields**:
*   **General Info**: Agent Code, Agent Name, Status (Active/Inactive), Email, Mobile.
*   **Commission**: Project, Unit, W.E.F (Effective Date), Commission Type, Commission Value.

### 1.5 Call Log
**Context**: A read-only history of telephonic interactions automatically logged or manually entered.
**Navigation**: CRM > Call Log
**Fields**:
*   **Log Data**: Incoming/Outgoing status, Timestamp, Duration, Caller ID.

### 1.6 Contacts
**Context**: A central repository of all people identifying detailed profiles of customers, partners, and stakeholders.
**Navigation**: CRM > Contacts
**Fields**:
*   **Identity**: Salutation, First Name, Last Name, Job Title, Company.
*   **Communication**: Mobile, Landline, Email.
*   **Address**: Address 1-3, City, State, Country, Zip.

---

## 2. Property Module (Asset Management)
**Keywords**: real estate, apartment, villa, plot, project, amenitites

### 2.1 Project Master
**Context**: The master entity representing a real estate development. All units and sectors belong to a project.
**Navigation**: Property > Project
**Fields**:
*   **General Info**: Project Name, Project Type, Property Category, Area (acres), Address, Geo-coordinates (Lat/Long).
*   **Marketing**: Project Location URL, Project Video URL, Short Description.
*   **Configuration**: Amenities linkage, Commission structures.

### 2.2 Sector
**Context**: Defines phases or sub-divisions within a larger project.
**Navigation**: Property > Sector
**Fields**:
*   **Details**: Name, Code, Status, Related Project.

### 2.3 Unit Master
**Context**: Represents the distinct saleable entity (e.g., "Flat 101", "Villa A", "Plot 5").
**Navigation**: Property > Unit
**Fields**:
*   **Specs**: Name, Code, Project, Area, UOM, Dimensions, Facing.
*   **Status**: Available, Sold, Blocked.
*   **Pricing**: UOM Price, PLC (Preferential Location Charges).

### 2.4 Amenities
**Context**: Manages the list of features available in a project (e.g., Gym, Pool).
**Navigation**: Property > Amenities
**Fields**:
*   **Details**: Name, Status, Photo/Icon Upload.

### 2.5 Testimonials
**Context**: Captures customer feedback for marketing display.
**Navigation**: Property > Testimonials
**Fields**:
*   **Content**: Project, Customer Name, Status, Feedback Text, Star Rating (1-5).

---

## 3. Inventory Module (Trading & Sales)
**Keywords**: stock, quote, invoice, order, procurement, billing

### 3.1 Products
**Context**: Catalog of non-property items helps in managing materials or services not classified as real estate units.
**Navigation**: Inventory > Products
**Fields**:
*   **Details**: Product Code, Name, Type (General/Service), Status, Unit (UOM), Category.
*   **Pricing**: Purchase Rate, Sale Rate.

### 3.2 Sales Quotation
**Context**: Issuing an official price estimate to a prospect. Often the first step in the financial commitment.
**Navigation**: Inventory > Sales Quotation
**Fields**:
*   **Header**: Doc Date, Doc No, Opportunity, Project, Agent.
*   **Line Items**: Product/Unit, Facing, Area, Rate, Gross Amount.
*   **Footer**: Terms & Conditions.

### 3.3 Sales Order
**Context**: Processing a confirmed order. This blocks the inventory/unit.
**Navigation**: Inventory > Sales Order
**Fields**:
*   **Details**: Doc Date, Opportunity, Project, Agent.
*   **Financials**: Unit Selection, Rate, Gross, Commission Details, Net Value.

### 3.4 Delivery Challan
**Context**: Documentation accompanying the physical handover or shipment of goods.
**Navigation**: Inventory > Delivery Challan
**Fields**:
*   **Details**: Doc Date, Customer, Sales Account, Items Grid.

### 3.5 Sales Invoice
**Context**: The final demand for payment. Recognizes revenue.
**Navigation**: Inventory > Sales Invoice
**Fields**:
*   **Details**: Doc Date, Opportunity, Project, Agent.
*   **Grid**: Unit/Item, Area, Rate, Gross, Tax (GST), Net Amount.

### 3.6 Sales Return (Credit Note)
**Context**: Handling returns of goods or cancellations requiring refund/adjustment.
**Navigation**: Inventory > Sales Return
**Fields**:
*   **Details**: Doc Date, Sales Account, Customer, Return Qty, Credit Amount.

### 3.7 Procurement (Purchase Cycle)
**Context**: Managing the buying of materials from vendors.
**Submodules**:
*   **Purchase Requisition**: Internal request for materials. Navigation: Inventory > Purchase Requisition.
*   **Purchase Quotation**: Logging vendor quotes. Navigation: Inventory > Purchase Quotation.
*   **Goods Received (GRN)**: Stock entry upon receipt. Navigation: Inventory > Goods Received.
*   **Purchase Invoice**: Liability creation for vendor payment. Navigation: Inventory > Purchase Invoice.
*   **Purchase Return**: Returning defective goods (Debit Note). Navigation: Inventory > Purchase Return.

### 3.8 Master Data
**Context**: Auxiliary inventory settings.
**Submodules**:
*   **UOM**: Unit of Measurement definitions (Nos, Kg, Sqft).
*   **Terms & Conditions**: Legal text snippets for document footers.

---

## 4. Finance Module
**Keywords**: accounts, ledger, receivable, payable

### 4.1 Customers (Accounts Receivable)
**Context**: Financial profiles of clients.
**Navigation**: Finance > Customers
**Fields**:
*   **General**: Account Code, Name, Group, Status, Credit Limit/Days.
*   **Contact**: Address Name, Contact Person, Billing Address.

### 4.2 Vendors (Accounts Payable)
**Context**: Financial profiles of suppliers.
**Navigation**: Finance > Vendors
**Fields**:
*   **Details**: Vendor Code, Name, Group, Status, Contact Person.

### 4.3 Accounts
**Context**: General ledger and Chart of Accounts management.
**Navigation**: Finance > Accounts

---

## 5. EMS & HR Module
**Keywords**: employee, staff, hr, payroll

### 5.1 Employee Master
**Context**: Records for all internal staff members.
**Navigation**: EMS > Employee
**Fields**:
*   **Official**: Employee ID, Name, Department, Grade, Job Title, Manager.
*   **Personal**: Nationality, Gender, DOB, Marital Status.
*   **Identity**: Passport Number, Issuing Country.

---

## 6. Masters Module
**Context**: System-wide configuration tables used in dropdowns across modules.
**Keywords**: config, settings, lookup, location, city

*   **Location**: Geo-locations and zones. Navigation: Masters > Location.
*   **Division**: Organizational divisions. Navigation: Masters > Division.
*   **Salesman**: Sales personnel registry. Navigation: Masters > Salesman.
*   **Category**: Classifiers for items/properties. Navigation: Masters > Category.
*   **Department**: Internal departments. Navigation: Masters > Department.
*   **Country/State**: Geo-political definitions. Navigation: Masters > Country / State.
*   **Lookups**: Generic system dropdowns. Navigation: Masters > Lookups.

---

## 7. Reports Module
**Context**: Analytics engine for visualization and export.
**Keywords**: analytics, charts, kpi

*   **Reports**: Tabular reports with export capabilities. Navigation: Reports > Reports.
*   **Widgets**: Configuration of KPI logic. Navigation: Reports > Widgets.
*   **Dashboards**: Visual canvas for widgets. Navigation: Reports > Dashboards.

---

## 8. Admin Module
**Context**: Control panel for system configuration, security, and automation.
**Keywords**: security, user, role, permission, workflow

*   **User/Role**: Access management.
*   **Settings**: List, Form, and Document settings.
*   **Workflow**: Approval logic design.
*   **Configuration**: Global parameters (Email, WhatsApp, Notifications).
*   **Data Tools**: Import, Bulk Delete.

---

## 9. Business Workflows
**Context**: Standard operating procedures describing how modules interact.

### 9.1 Lead to Cash (Sales Cycle)
1.  **Capture**: Create **Lead** (CRM).
2.  **Qualify**: Convert Lead to **Opportunity** (CRM).
3.  **Quote**: Generate **Sales Quotation** (Inventory) linked to Project/Unit.
4.  **Close**: Confirm **Sales Order** (Inventory) to block unit.
5.  **Bill**: Raise **Sales Invoice** (Inventory).
6.  **Collect**: Record payment against Invoice (Finance).

### 9.2 Procure to Pay (Purchase Cycle)
1.  **Request**: Raise **Purchase Requisition** (Inventory).
2.  **Source**: Log **Purchase Quotation** from vendor.
3.  **Receive**: Create **Goods Received Note (GRN)** upon delivery.
4.  **Bill**: Log **Purchase Invoice** (Bill).
5.  **Pay**: Process payment to Vendor (Finance).

---

## 10. Integrations
**Context**: External system connections for enhanced functionality.

### 10.1 WhatsApp Integration
**Functional Description**: Automated engagement tool.
**Triggers**:
*   Welcome message upon Lead creation.
*   Quote PDF delivery.
*   Payment reminders.
**Configuration**: Managed via `Admin > Whatsapp Config`.

### 10.2 AI Assistant
**Functional Description**: Natural Language Query (NLQ) interface for real-time data retrieval.
**Capabilities**:
*   "How many new leads did I get today?"
*   "Show me pending tasks."
**Security**: Respects User Role/Data Scope (e.g., Salesperson sees only their leads, Admin sees all).
**Access**: Accessible via the Robot icon in the top navigation bar.
.
"""
