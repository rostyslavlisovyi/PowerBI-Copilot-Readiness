# Business Glossary — Copilot Readiness Context

> Source of truth for the agent when writing/normalizing descriptions (PBI-031 branch A/B).
> The agent NEVER invents business context — it draws only from this file and the model's own DAX.
> Granularity: business TERMS, not individual measures. The agent combines a term's
> meaning here with a measure's DAX to produce a <=200-char description.

| Term | Definition | Usage rule | Unit / Format | Synonyms | Related field / measure |
|---|---|---|---|---|---|
| Active User | Unique user with >=1 CRM activity event in context | Base user metric; always apply a date filter to avoid all-time counts | count | active user, user | Active Users; User Identifier |
| User Identifier | Unified user key combining User ID, User Email, PostHog Distinct ID | Use for max user coverage across identification methods | key | user key | User Identifier |
| DAU / WAU / MAU | Unique active users over 1 / 7 / 30 complete trailing days ending yesterday | Full-day windows only; independent of date slicer | count | daily/weekly/monthly active users | Daily/Weekly/Monthly Active Users |
| Stickiness | WAU / MAU ratio; share of monthly users active weekly | Habitual engagement; 80%+ excellent, 60-80% healthy, <40% critical | % | engagement ratio | Stickiness |
| Instance | A separate client CRM deployment / hosted environment | Deployment-level analysis unit | count | client instance, deployment | Active Instances; CRM Instance Name |
| Service | A CRM service (e.g. Cloud CRM, GeoForce, Cycle Plan, Admin Tool) | Service-level engagement breadth | count | CRM service | Active Services; CRM Service Name |
| Module | A CRM module (e.g. Schedule, Contacts, Companies, Reports) | Feature-adoption breadth | count | CRM module, feature | Active Modules; CRM Module Name |
| Event | A single CRM activity interaction (pre-aggregated daily per user/module) | Depth of use vs breadth (users) | count | activity event | Total Events; Event Count |
| Application Version | Production version of CRM app per platform (Flutter.Mobile / Flutter.Web) | Requires single Platform selection | text | app version | Current Application Version |
| Current vs Legacy Version | Users on latest prod version vs older version | Adoption / upgrade-gap analysis | count / % | current/outdated/legacy | Current Version Adoption %; Users on Legacy Version |
| Report Session | One Power BI report opening by a user | Primary Power BI adoption metric | count | session | Total Report Sessions |
| WoW / MoM Change | Change vs same day/period one week/month earlier | Trend context on KPI cards | count / % | week-over-week, month-over-month | DAU WoW Change; MAU MoM Change |
| Data Refresh | Timestamp of last semantic model data update | Show data freshness to users | datetime | last refresh | Last Data Refresh |
| Country | Country where the event was recorded, as reported by the user's device to the analytics (PostHog) server. Reflects the device's apparent location -- actual physical location, or a masked/VPN location if the user is using a VPN | Device-reported, not verified against CRM instance region; treat as approximate geography, not an authoritative user/company location | text | user country, event country, geographic location | Application Usage Events[Country]; Power BI Usage Events[Country] |
| Platform | Client platform that generated the event: Web (browser-based Proxima CRM) or Mobile (Flutter app installed on a phone/tablet) | Single-select per event; aligns with the Web/Mobile split already used for Application Version | text (Web / Mobile) | client platform, device type, app platform | Platform; Application Version |
| User Role | The user's role within the CRM system -- a named permission group for a set of users (e.g. Administrator, or a regional role such as "РМ Україна" / Regional Manager Ukraine) | Role names are CRM-specific (organization-defined), not a generic admin/user/viewer scale; use for segmenting usage by permission tier or regional responsibility | text (role name) | CRM role, permission group, job role | User Role |
