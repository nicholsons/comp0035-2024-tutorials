# A solution to week 4 ERD

![tutorial4_erd.png](tutorial4_erd.png)

## Enable mermaid support

The diagram in the markdown below uses [Mermaid](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) to define
and display database diagrams. To view the diagram in the markdown you need to have this tool installed.

For PyCharm, Go to PyCharm | Settings | Plugins then search for
the [Mermaid plugin](https://plugins.jetbrains.com/plugin/20146-mermaid).

For VS Code, go to Code | Settings | Extensions and find
the [Mermaid chart extension](https://marketplace.visualstudio.com/publishers/MermaidChart).

## ERD

SQLite does not have a ['date' data type](https://www.sqlite.org/lang_datefunc.html). Dates can be stored as text or
integer.

```mermaid
erDiagram
    event {
        int event_id PK
        int type "NOT NULL"
        int year "NOT NULL"
        text start "format: dd/mm/yyyy"
        text end "format: dd/mm/yyyy"
        text disabilities
        int countries
        int events
        int sports
        int participants_m
        int participants_f
        int participants
        text highlights
        text url
    }

    country {
        text code PK
        text name "NOT NULL"
        text region
        text sub_region
        text member_type
        text notes
    }

    host {
        int host_id PK
        text country_code FK "ON DELETE CASCADE ON UPDATE CASCADE"
        text host "NOT NULL"
    }

    host_event {
        int host_id FK "ON DELETE CASCADE ON UPDATE CASCADE"
        int event_id FK "ON DELETE CASCADE ON UPDATE CASCADE"
    }

    event ||--o{ host_event: "hosted by"
    host ||--o{ host_event: hosts
    host }o--|| country: "is in"
```