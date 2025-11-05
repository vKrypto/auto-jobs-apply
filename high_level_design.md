## 1. System Architecture

```mermaid
graph TB
    subgraph "Frontend"
        UI[React + TypeScript<br/>Port 3000]
    end
  
    subgraph "Backend"
        API[FastAPI Server<br/>Port 5000]
        CTRL[Controller]
        SERVICES[Services Layer]
    end
  
    subgraph "Services"
        JS[Job Scraper]
        AI[AI Service]
        APS[Application Service]
    end
  
    subgraph "Data"
        DB[(Database)]
    end
  
    subgraph "External"
        OPENAI[OpenAI API]
        JOBS[Job Boards]
    end
  
    UI -->|HTTP POST| API
    API --> CTRL
    CTRL --> SERVICES
    SERVICES --> JS
    SERVICES --> AI
    SERVICES --> APS
    JS --> JOBS
    AI --> OPENAI
    APS --> JOBS
    SERVICES --> DB
```

---

## 2. Auto-Apply Flow

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Services
    participant External
  
    User->>Frontend: Click "Auto Apply"
    Frontend->>Backend: POST /api/auto-apply
  
    Backend->>Services: Execute Auto-Apply
  
    Services->>External: 1. Scrape Jobs
    External-->>Services: Job List
  
    Services->>External: 2. AI Select Best Job
    External-->>Services: Selected Job
  
    Services->>External: 3. AI Generate Cover Letter
    External-->>Services: Cover Letter
  
    Services->>External: 4. Submit Application
    External-->>Services: Result
  
    Services->>Backend: Response
    Backend->>Frontend: Success/Failure
    Frontend->>User: Display Status
```

---

## 3. Component Structure

```mermaid
graph LR
    subgraph "Frontend"
        APP[App]
        BTN[AutoApplyButton]
        STATUS[StatusDisplay]
    end
  
    subgraph "Backend"
        CTRL[Controller]
        AS[Auto Apply Service]
        JS[Job Scraper]
        AI[AI Service]
        APS[Application Service]
    end
  
    APP --> BTN
    APP --> STATUS
    BTN --> CTRL
    CTRL --> AS
    AS --> JS
    AS --> AI
    AS --> APS
```

---

## 4. Data Flow

```mermaid
flowchart LR
    START([User Action]) --> PREFS[Preferences]
    PREFS --> SCRAPE[Scrape Jobs]
    SCRAPE --> SELECT[AI Select Job]
    SELECT --> COVER[Generate Cover Letter]
    COVER --> APPLY[Submit Application]
    APPLY --> RESULT[Result]
    RESULT --> SAVE[Save to DB]
    SAVE --> DISPLAY[Display Status]
```

---

## Technology Stack

- **Frontend**: React, TypeScript, Vite
- **Backend**: FastAPI, Python
- **AI**: OpenAI API
- **Database**: PostgreSQL
- **Architecture**: Layered (Presentation → API → Service → Data)
