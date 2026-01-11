def build_prompt(student, jd):
    return f"""
You are an AI assistant for an internship platform called InternHub.

Student Profile:
Name: {student.name}
Skills: {student.skills}
Interests: {student.interests}
Experience: {student.experience}

Internship Description:
{jd}

Tasks:
1. Internship Match Summary
2. Skill Gap Explanation
3. Improvement Recommendations

IMPORTANT:
You MUST include the resume between the exact delimiters below.

=== RESUME (START) ===
<resume content here>
=== RESUME (END) ===

Do NOT change the delimiter text.


5. ATS Confidence Score (0 - 100)

IMPORTANT:
Keep the resume clean and structured.
"""
