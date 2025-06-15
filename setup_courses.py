#!/usr/bin/env python3
"""
Level AI Academy Course Setup Script
Creates the 5-level UK Government AI Playbook course structure in Frappe LMS
"""

import frappe
import json

def setup_level_ai_academy():
    """Set up the complete Level AI Academy course structure"""
    
    # Ensure we're in the right site context
    frappe.init(site='lms.localhost')
    frappe.connect()
    
    # Create Level AI Academy course categories
    categories = [
        {
            "title": "Level 1: AI Foundations",
            "description": "Understanding AI: From Buzzword to Breakthrough",
            "category_name": "level-1-foundations",
            "color": "#feda00",  # Sunshine Yellow
            "level": 1
        },
        {
            "title": "Level 2: AI User Competency", 
            "description": "From Observer to Operator: Mastering AI Tools",
            "category_name": "level-2-user-competency",
            "color": "#296b42",  # Terra Green
            "level": 2
        },
        {
            "title": "Level 3: AI Implementation Professional",
            "description": "Building Solutions: From Concept to Reality", 
            "category_name": "level-3-implementation",
            "color": "#ff7f7a",  # Coral
            "level": 3
        },
        {
            "title": "Level 4: AI Strategic Leadership",
            "description": "Leading the Revolution: AI Strategy for Purpose-Driven Leaders",
            "category_name": "level-4-strategic-leadership", 
            "color": "#293f3b",  # Earthstone
            "level": 4
        },
        {
            "title": "Level 5: AI Innovation and Advanced Practice",
            "description": "Pioneering Impact: Leading AI Innovation for Social Good",
            "category_name": "level-5-innovation",
            "color": "#1a4d2e",  # Deep Terra
            "level": 5
        }
    ]
    
    # Create categories
    for cat in categories:
        if not frappe.db.exists("LMS Category", cat["category_name"]):
            doc = frappe.get_doc({
                "doctype": "LMS Category",
                "title": cat["title"],
                "name": cat["category_name"],
                "description": cat["description"],
                "category_name": cat["category_name"]
            })
            doc.insert()
            print(f"Created category: {cat['title']}")
    
    # Create Level 1: AI Foundations Course
    level1_course = {
        "doctype": "LMS Course",
        "title": "Level 1: AI Foundations - Understanding AI: From Buzzword to Breakthrough",
        "short_introduction": "Complete beginner's guide to AI for charity and social enterprise staff. Learn what AI really is, how it can help your mission, and build essential AI literacy.",
        "description": """
        <h2>Course Overview</h2>
        <p><strong>Duration:</strong> 2-4 weeks (8-12 hours total)<br>
        <strong>Target:</strong> Complete beginners, all staff levels<br>
        <strong>Prerequisites:</strong> None - perfect for first-time learners</p>
        
        <h3>What You'll Learn</h3>
        <ul>
            <li>Demystify AI - understand what AI actually is and isn't</li>
            <li>Explore real-world AI applications in charity work</li>
            <li>Learn about AI capabilities and limitations</li>
            <li>Understand AI ethics and responsible use</li>
            <li>Build foundation knowledge for practical AI adoption</li>
        </ul>
        
        <h3>Learning Outcomes</h3>
        <p>By the end of this course, you'll have:</p>
        <ul>
            <li>✅ Clear understanding of AI fundamentals</li>
            <li>✅ Ability to identify AI opportunities in your work</li>
            <li>✅ Knowledge of ethical AI principles</li>
            <li>✅ Confidence to engage in AI discussions</li>
            <li>✅ Readiness to progress to Level 2: AI User Competency</li>
        </ul>
        """,
        "course_intro": "Welcome to Level 1: AI Foundations - your first step into the world of AI for social good!",
        "category": "level-1-foundations",
        "is_published": 1,
        "enable_certification": 1,
        "paid_course": 0,
        "price": 0,
        "currency": "GBP",
        "upcoming": 0,
        "disable_self_learning": 0,
        "medium": "Online",
        "published": 1
    }
    
    # Create the course if it doesn't exist
    if not frappe.db.exists("LMS Course", {"title": level1_course["title"]}):
        course_doc = frappe.get_doc(level1_course)
        course_doc.insert()
        print(f"Created course: {level1_course['title']}")
        
        # Create course chapters and lessons
        create_level1_content(course_doc.name)
    
    frappe.db.commit()
    print("Level AI Academy course structure created successfully!")

def create_level1_content(course_name):
    """Create detailed content for Level 1: AI Foundations"""
    
    # Week 1: What Actually Is AI?
    week1_chapter = frappe.get_doc({
        "doctype": "Course Chapter",
        "title": "Week 1: What Actually Is AI?",
        "course": course_name,
        "chapter_description": "Demystify AI and understand what it really means for your charity work",
        "idx": 1
    })
    week1_chapter.insert()
    
    # Lesson 1.1: AI Demystified
    lesson_1_1 = frappe.get_doc({
        "doctype": "LMS Topic",
        "title": "1.1: AI Demystified - Understanding AI in Plain English",
        "chapter": week1_chapter.name,
        "course": course_name,
        "content": """
        <h2>AI Explained in 3 Minutes</h2>
        
        <div class="video-container">
            <p><strong>Video Script:</strong> "AI Explained in 3 Minutes"</p>
            <blockquote>
            <p>Right, let's clear this up once and for all. AI isn't robots taking over the world—it's actually much more mundane and much more useful than that.</p>
            
            <p>Think of AI as a very good pattern-spotter. If you show it enough examples of something, it gets brilliant at recognising similar things later.</p>
            
            <p>Like this: A child learns to recognise dogs by seeing lots of dogs. AI does the same thing, but with data instead of photos, and much, much faster.</p>
            
            <p><strong>Three types you'll actually encounter:</strong></p>
            <ol>
                <li><strong>Simple AI</strong> - Like spell-check or recommended films on Netflix</li>
                <li><strong>Smart AI</strong> - Like ChatGPT or voice assistants</li>
                <li><strong>Fancy AI</strong> - Like medical diagnosis or climate modelling</li>
            </ol>
            
            <p>For your charity? You'll mainly use type 2. And that's perfectly fine—it's already game-changing.</p>
            
            <p><strong>Bottom line:</strong> AI is a powerful tool that can help you do your job better, faster, and sometimes more creatively. It's not magic, it's not conscious, and it definitely can't replace your judgment about what matters to your beneficiaries.</p>
            </blockquote>
        </div>
        
        <h3>Interactive Exercise: Spot the AI</h3>
        <p>Drag and drop these examples into the correct AI category:</p>
        <ul>
            <li>Netflix recommendations → Simple AI</li>
            <li>ChatGPT writing assistance → Smart AI</li>
            <li>Spell checker in Word → Simple AI</li>
            <li>Medical imaging diagnosis → Fancy AI</li>
            <li>Siri voice assistant → Smart AI</li>
        </ul>
        
        <h3>Reflection Questions</h3>
        <ol>
            <li>What AI tools do you already use in your daily life without realising?</li>
            <li>How might pattern recognition help your charity's work?</li>
            <li>What's one AI myth you believed before this lesson?</li>
        </ol>
        """,
        "topic_type": "Article",
        "idx": 1
    })
    lesson_1_1.insert()
    
    # Lesson 1.2: AI in the Wild
    lesson_1_2 = frappe.get_doc({
        "doctype": "LMS Topic", 
        "title": "1.2: AI in the Wild - How Charities Are Actually Using AI",
        "chapter": week1_chapter.name,
        "course": course_name,
        "content": """
        <h2>Real Charity AI Success Stories</h2>
        
        <div class="case-study">
            <h3>Crisis Homeless Charity</h3>
            <p><strong>Challenge:</strong> Limited outreach resources, need to prioritise which rough sleepers to help first</p>
            <p><strong>AI Solution:</strong> Predictive analytics to identify highest-risk individuals</p>
            <p><strong>Result:</strong> 40% improvement in engagement rates</p>
            <p><strong>Lesson:</strong> AI helps prioritise human resources for maximum impact</p>
        </div>
        
        <div class="case-study">
            <h3>Age UK</h3>
            <p><strong>Challenge:</strong> Overwhelming number of common queries taking staff time from complex cases</p>
            <p><strong>AI Solution:</strong> Chatbot for 24/7 basic information and signposting</p>
            <p><strong>Result:</strong> Staff freed up for meaningful human connections</p>
            <p><strong>Lesson:</strong> AI handles routine so humans can focus on what matters</p>
        </div>
        
        <div class="case-study">
            <h3>The National Trust</h3>
            <p><strong>Challenge:</strong> Thousands of historical documents need digitising and searching</p>
            <p><strong>AI Solution:</strong> Automated transcription and content recognition</p>
            <p><strong>Result:</strong> Decades of work reduced to months</p>
            <p><strong>Lesson:</strong> AI accelerates time-consuming but important tasks</p>
        </div>
        
        <h3>The Pattern</h3>
        <p>Notice what all these examples have in common:</p>
        <ul>
            <li>✅ AI handles the time-consuming, repetitive stuff</li>
            <li>✅ Humans focus on impact, creativity, and care</li>
            <li>✅ The mission is enhanced, not replaced</li>
            <li>✅ Beneficiaries get better service</li>
        </ul>
        
        <h3>Your Turn: AI Opportunity Spotter</h3>
        <p>Think about your own organisation and complete this worksheet:</p>
        
        <div class="worksheet">
            <h4>Repetitive Tasks in My Work</h4>
            <ol>
                <li>What task do you do repeatedly that feels time-consuming? ________________</li>
                <li>How much time does this take per week? ________________</li>
                <li>Could pattern recognition help with this task? ________________</li>
                <li>What would you do with that time if it was freed up? ________________</li>
            </ol>
            
            <h4>Communication Challenges</h4>
            <ol>
                <li>What questions do people ask your organisation repeatedly? ________________</li>
                <li>How could instant, accurate answers help your beneficiaries? ________________</li>
                <li>What complex conversations need human empathy and judgement? ________________</li>
            </ol>
        </div>
        """,
        "topic_type": "Article",
        "idx": 2
    })
    lesson_1_2.insert()
    
    # Week 2: Capabilities and Limitations
    week2_chapter = frappe.get_doc({
        "doctype": "Course Chapter",
        "title": "Week 2: What AI Can and Cannot Do",
        "course": course_name,
        "chapter_description": "Understanding AI's superpowers and limitations to use it effectively and safely",
        "idx": 2
    })
    week2_chapter.insert()
    
    # Add quiz for Week 1
    quiz_week1 = frappe.get_doc({
        "doctype": "LMS Quiz",
        "title": "Week 1 Knowledge Check: AI Fundamentals",
        "course": course_name,
        "quiz_type": "Formal Quiz"
    })
    quiz_week1.insert()
    
    print(f"Created Level 1 content structure for course: {course_name}")

if __name__ == "__main__":
    setup_level_ai_academy()