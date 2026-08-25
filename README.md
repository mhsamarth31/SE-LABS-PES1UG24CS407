# SE Lab 1 – Requirements Engineering & UML Use-Case Modelling

**Course:** Software Engineering Lab | PES University  
**Problem Statement:** #39 – Retail, E-Commerce & Finance  
**System:** Second-Hand Product Escrow Marketplace  

---

## Problem Overview

A secure peer-to-peer trading marketplace where:
- Buyer payments are **held in escrow** upon order placement
- An independent **Inspection Agent** physically verifies the product condition
- Escrow funds are **released to the seller only** after the buyer reviews the inspection result and provides explicit sign-off
- A buyer-raised **dispute immediately freezes** the escrow funds until resolution

---

## Repository Structure

```
SE-Lab1-SecondHand-Escrow/
├── README.md
├── requirements/
│   └── Requirements_Table.xlsx
├── uml/
│   └── Use_Case_Diagram.pdf
└── use-case-flow/
    └── Use_Case_Flow.pdf
```

---

## Deliverable 1 – Requirements Table

**File:** `requirements/Requirements_Table.docx` / `.xlsx`

### Functional Requirements

| Req ID | Description | Priority |
|--------|-------------|----------|
| FR-001 | System shall lock buyer payment in escrow and transition order state to *Under Inspection* until an inspection agent submits physical verification sign-off. | High |
| FR-002 | System shall allow a buyer to select an available second-hand product and initiate a purchase by submitting the required order and payment details. | High |
| FR-003 | System shall assign an inspection request to an inspection agent and allow the agent to record the product's physical verification result. | High |
| FR-004 | System shall allow the buyer to review the inspection result and provide explicit sign-off; only after valid sign-off shall the escrow payment be released to the seller. | High |
| FR-005 | System shall allow the buyer to raise a dispute when the inspection result or delivered product is not acceptable, and shall place the related escrow funds on hold while the dispute is active. | High |

### Non-Functional Requirements

| Req ID | Type | Description | Priority |
|--------|------|-------------|----------|
| NFR-001 | Performance & Security | System shall freeze escrow funds immediately when a dispute-resolution ticket becomes active and prevent withdrawals during the investigation. | High |
| NFR-002 | Security | System shall protect buyer personal and payment information using encryption in transit and at rest, and restrict access to authorized roles only. | High |

> FR-001 and NFR-001 are based on the requirements supplied in the problem statement. FR-002–FR-005 and NFR-002 are derived from the stated marketplace scenario and its escrow/inspection workflow.

---

## Deliverable 2 – UML Use-Case Diagram

**File:** `uml/Use_Case_Diagram.pdf`

### Actors

| Actor | Type | Role |
|-------|------|------|
| Buyer | Primary | Places orders, reviews inspection results, signs off or raises disputes |
| Inspection Agent | Primary | Physically verifies product condition and submits report |
| Payment Gateway | External System | Authorizes and processes buyer payments |

### Use Cases

| ID | Use Case |
|----|----------|
| UC-01 | Purchase Product |
| UC-02 | Make Payment |
| UC-03 | Hold Payment in Escrow |
| UC-04 | Perform Product Inspection |
| UC-05 | Review Inspection & Sign Off |
| UC-06 | Raise Dispute |

### UML Relationships

| Relationship | From | To | Reason |
|---|---|---|---|
| `«include»` | Purchase Product | Make Payment | Purchasing always requires payment |
| `«include»` | Make Payment | Hold Payment in Escrow | Payment always triggers escrow lock |
| `«extend»` | Raise Dispute | Review Inspection & Sign Off | Dispute is raised optionally at sign-off step |

---

## Deliverable 3 – Use-Case Flow Specification

**File:** `use-case-flow/Use_Case_Flow.docx` / `.pdf`  
**Use Case:** Complete Purchase with Inspection and Escrow  
**Primary Actor:** Buyer  
**Supporting Actors:** Inspection Agent, Payment Gateway  

### Preconditions
- Buyer is authenticated and has selected an available product
- Product is eligible for inspection and payment service is available
- An inspection agent is available to perform verification

### Main Success Scenario (11 steps)
1. Buyer selects product and chooses Purchase
2. System creates the order and requests payment details
3. Buyer submits valid payment details
4. Payment Gateway authorizes the payment
5. System locks the authorized amount in escrow → order state: *Under Inspection*
6. System creates an inspection request and assigns it to an Inspection Agent
7. Inspection Agent examines the product and submits physical verification result
8. System stores the inspection result and notifies the Buyer
9. Buyer reviews the result and provides explicit sign-off
10. System changes escrow status to *Released* and releases payment to seller
11. System marks transaction as *Completed* and confirms to Buyer

### Alternate Flow – Buyer Raises a Dispute
- **9a1.** At Step 9, Buyer rejects the result and selects *Raise Dispute*
- **9a2.** System creates a dispute ticket and immediately freezes escrow funds
- **9a3.** System blocks withdrawal/release of disputed amount while dispute is active and notifies all parties
- **9a4.** Use case ends in *Dispute Pending*; escrow is not released

### Postconditions
- **Success path:** Escrow released, transaction marked *Completed*
- **Alternate path:** Escrow frozen, transaction in *Dispute Pending*

---

## Submission Checklist

- [x] Exactly 5 Functional Requirements (FR-001 to FR-005)
- [x] Exactly 2 Non-Functional Requirements (NFR-001 and NFR-002)
- [x] All rows include: ID, Type, Description, Priority, Acceptance Criteria, Rationale
- [x] At least 3 actors in the UML diagram
- [x] At least 5 use cases in the UML diagram
- [x] At least one `«include»` relationship
- [x] At least one `«extend»` relationship
- [x] Preconditions documented
- [x] Postconditions documented
- [x] Main success scenario documented
- [x] At least one alternate flow documented