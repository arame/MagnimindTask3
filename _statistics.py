import re
from _utility import gl
def get_summary_statistics(df, df_jobs):
    get_perc = lambda x, y: round(len(x)/len(y)*100, 2)
    
    print(f"There are {len(df)} job descriptions")
    df_ = df[df.duplicated()]
    print(f"Of which {get_perc(df_, df_jobs)}% are duplicated")
    df_ = df[df[gl.title].str.contains(pat = 'Data Scie', case=False)]
    print(f"Of which {get_perc(df_, df_jobs)}% are specified as Data Science jobs in their job titles")
    df_ = df[df[gl.title].str.contains(pat = 'Computer Vision', case=False)]
    print(f"Of which {get_perc(df_, df_jobs)}% are specified as Computer Vision jobs in their job titles")
    re_pattern = re.compile(r'\b(?:natural language processing|NLP)(?<!\w\B)',re.IGNORECASE)
    df_ = df[df[gl.title].str.contains(pat = re_pattern, regex=True)]
    print(f"Of which {get_perc(df_, df_jobs)}% are specified as NLP jobs in their job titles")
    re_pattern = re.compile(r'\b(?:AI|A[.]I[.]|artificial)(?<!\w\B)',re.IGNORECASE)
    df_ = df[df[gl.title].str.contains(pat = re_pattern, regex=True)]
    print(f"Of which {get_perc(df_, df_jobs)}% are specified as AI jobs in their job titles")
    
    list_lookup = ['Python', 'years', 'experience', 'skills', 'Scikit-Learn', 'GeonamesCache',
        'Dimensionality', 'K-Means']
    for item in list_lookup:
        df_ = df_jobs[df_jobs[gl.bullet_points].str.contains(pat = item, case=False)]
        print(f"Of which {get_perc(df_, df_jobs)}% are specifying {item} in their bullet points")

    tot_no_bullet_points1 = df_jobs[gl.bullet_points].isnull().sum()
    tot_no_bullet_points2 = (df_jobs[gl.bullet_points] == '').sum()
    tot_no_bullet_points_perc = round((tot_no_bullet_points1 + tot_no_bullet_points2)/ len(df_jobs) * 100, 2)
    print(f"Of which {tot_no_bullet_points_perc}% do not have any bullet points")
    df_ = df_jobs[df_jobs[gl.body].str.contains(pat = 'Statistical Modelling', case=False)]
    print(f"Of which {get_perc(df_, df_jobs)}% are specifying Statistical Modelling in the job description")
    list_lookup = ['Python', 'years', 'experience', 'skills', 'Scikit-Learn', 'GeonamesCache',
        'Dimensionality', 'K-Means']
    for item in list_lookup:
        df_ = df[df[gl.bullet_points].str.contains(pat = item, case=False)]
        print(f"Of which {get_perc(df_, df_jobs)}% are specifying {item} in their bullet points")
    
    tot_no_bullet_points1 = df[gl.bullet_points].isnull().sum()
    tot_no_bullet_points2 = (df[gl.bullet_points] == '').sum()
    tot_no_bullet_points_perc = round((tot_no_bullet_points1 + tot_no_bullet_points2)/ len(df) * 100, 2)
    print(f"Of which {tot_no_bullet_points_perc}% do not have any bullet points")
    df_ = df[df[gl.body].str.contains(pat = 'Statistical Modelling', case=False)]
    print(f"Of which {get_perc(df_, df_jobs)}% are specifying Statistical Modelling in the job description")