from src.jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
    search_term="django engineer",
    location="Detroit, MI",
    results_wanted=5,
    country_indeed='USA'  # only needed for indeed / glassdoor
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_excel("jobs.xlsx", index=False) # to_xlsx