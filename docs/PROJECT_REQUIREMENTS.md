# OLA Ride Operations Analytics — Project Requirements Document

**Project:** OLA Ride Operations Analytics Dashboard  
**Prepared by:** Rushi Wavhal  
**Date:** 10 October 2026  
**Tool:** Microsoft Power BI  
**Version:** 1.0

---

## 1. Project Overview

This project delivers an interactive Power BI dashboard for analyzing OLA ride-booking operations. It provides visibility into ride volume, revenue, cancellations, customer behaviour, and operational performance.

The solution supports data-driven decisions for operations, revenue, and customer-experience teams.

---

## 2. Business Problem

Ride-sharing businesses handle large volumes of booking, ride, customer, and revenue data. Without a centralized reporting solution, stakeholders struggle to identify:

- Revenue-driving locations and time periods
- High-cancellation zones and causes
- Peak demand hours
- Customer booking patterns
- Operational performance gaps

---

## 3. Project Goals

- Create a single interactive dashboard for ride-operations monitoring.
- Track revenue, rides, average fare, cancellations, and completion rate.
- Identify high-demand and high-risk operational areas.
- Enable drill-down analysis by time, location, ride type, and customer segment.
- Provide clear insights for business decision-making.

---

## 4. Scope

### In Scope

- Power BI dashboard development
- Data modelling and relationship design
- DAX-based KPI calculation
- Interactive filtering and visual analysis
- Executive, operational, revenue, and customer-focused report pages
- Dashboard documentation and presentation

### Out of Scope

- Live production database integration
- Real-time streaming data ingestion
- Advanced predictive machine-learning models
- Mobile application development

---

## 5. Stakeholders

| Stakeholder | Requirement |
|---|---|
| Operations Team | Monitor ride completion, cancellations, and demand patterns |
| Revenue Team | Analyze revenue, fare trends, and high-value segments |
| Management | Review high-level KPIs and business performance |
| Data Analyst | Explore data and generate actionable insights |

---

## 6. Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | Display total rides, revenue, average fare, cancellation rate, and completion rate |
| FR-02 | Allow filtering by date, location, ride type, and customer segment |
| FR-03 | Show ride-volume and revenue trends over time |
| FR-04 | Identify peak demand hours and days |
| FR-05 | Analyze cancellations by location, time, and ride category |
| FR-06 | Provide customer booking and repeat-ride insights |
| FR-07 | Enable drill-down from summary KPIs to detailed visuals |
| FR-08 | Present insights in a clean, executive-friendly layout |

---

## 7. Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR-01 | Dashboard should load and respond quickly to filters |
| NFR-02 | Visual design should be clean, consistent, and business-ready |
| NFR-03 | Measures should use optimized DAX logic |
| NFR-04 | Data model should support future additional reports |
| NFR-05 | Report should be understandable to non-technical stakeholders |

---

## 8. Data Requirements

The dashboard requires ride-level data including:

- Booking / ride ID
- Booking date and time
- Pickup and drop location
- Ride type or category
- Ride status
- Fare / revenue amount
- Distance
- Customer ID or segment
- Cancellation information

---

## 9. KPI Definitions

| KPI | Definition |
|---|---|
| Total Rides | Count of ride bookings in the selected period |
| Total Revenue | Sum of fare or revenue generated |
| Average Fare | Total revenue divided by total rides |
| Cancellation Rate | Cancelled rides divided by total rides |
| Completion Rate | Completed rides divided by total rides |
| Peak Demand | Time period with the highest ride volume |

---

## 10. Deliverables

- Power BI `.pbix` dashboard file
- Interactive multi-page report
- Dashboard screenshots
- Project requirements document
- Project presentation
- Business insights and recommendations

---

## 11. Expected Business Impact

- Improved visibility into operational performance
- Faster identification of revenue leakage
- Better driver and capacity planning during peak hours
- Data-backed customer retention and promotion strategy
- Improved decision-making through centralized KPI reporting
