# Data Model Specs

## Data Structure
- Each todo must have:
  - Unique ID
  - Title
  - Optional description
  - Completed status (true/false)
  - Created timestamp

## Storage Requirements
- Use a JSON file for persistence
- Automatically create the file if it does not exist
- Load todos on app start
- Save todos after every change
