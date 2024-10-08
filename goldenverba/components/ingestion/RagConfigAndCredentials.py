# Credentials configuration
credentials_default = {
    "credentials": {
        "deployment": "Weaviate",  # Change this as per your environment
        "url": "https://tiiateatrnkqtrpaypwqw.c0.asia-southeast1.gcp.weaviate.cloud",  # Weaviate URL
        "key": "7NOCz671EcnyXhid0VfpJ43yqh5XjODtIxlZ"  # Weaviate API key
    }
}

# RAG (Retrieval-Augmented Generation) Configuration for file imports
RagConfigForGeneration = {
    "rag_config": {
        "Reader": {
            "selected": "UnstructuredLibrary",  # Use the default reader
            "components": {
                "UnstructuredLibrary": {
                    "name": "UnstructuredLibrary",
                    "variables": [],
                    "library": [],
                    "description": "Ingests text, code, PDF, DOCX, and other common file types",
                    "config": {},
                    "type": "FILE",
                    "available": True
                }
            }
        },
        "Chunker": {
            "selected": "Token",  # Token-based chunker
            "components": {
                "Token": {
                    "name": "Token",
                    "variables": [],
                    "library": [],
                    "description": "Splits documents based on word tokens",
                    "config": {
                        "Tokens": {
                            "type": "number",
                            "value": 200,  # Adjust chunk size
                            "description": "Choose how many Tokens per chunk",
                            "values": []
                        },
                        "Overlap": {
                            "type": "number",
                            "value": 50,  # Overlap between chunks
                            "description": "Choose how many Tokens overlap between chunks",
                            "values": []
                        }
                    },
                    "type": "Token",  # Add the missing "type" field
                    "available": True
                }
            }
        },
        "Embedder": {
            "selected": "SentenceTransformers",  # Choose embedder
            "components": {
                "SentenceTransformers": {
                    "name": "SentenceTransformers",
                    "variables": [],
                    "library": ["sentence_transformers"],  # Required library
                    "description": "Embeds and retrieves objects using SentenceTransformer",
                    "config": {
                        "Model": {
                            "type": "dropdown",
                            "value": "all-MiniLM-L6-v2",  # Example model
                            "description": "Select a SentenceTransformers model",
                            "values": ["all-MiniLM-L6-v2", "all-mpnet-base-v2", "paraphrase-MiniLM-L6-v2"]
                        }
                    },
                    "type": "EMBEDDER",  # Add the missing "type" field
                    "available": True
                }
            }
        }
    }
}



# You can retain other settings like dimensions_AFE here without changes


dimensions_AFE = {
# Example structure, fill in with actual dimensions and sub-dimensions
      "Mastery of the Subject": {
            "weight": 0.169,
            "sub-dimensions": {
                "Knowledge of Content and Pedagogy": {
                    "weight": 0.362,
                    "definition": "A deep understanding of their subject matter and the best practices for teaching it.",
                    "example": "In a mathematics course on real analysis, the professor demonstrates best practices by Guiding students through the process of constructing formal proofs step-by-step, highlighting common pitfalls and techniques for overcoming them.",
                    "criteria": {
                        1: "The transcript demonstrates minimal knowledge of content and ineffective pedagogical practices",
                        2: "The transcript demonstrates basic content knowledge but lacks pedagogical skills",
                        3: "The transcript demonstrates adequate content knowledge and uses some effective pedagogical practices",
                        4: "The transcript demonstrates strong content knowledge and consistently uses effective pedagogical practices",
                        5: "The transcript demonstrates exceptional content knowledge and masterfully employs a wide range of pedagogical practices"
                    }
                },
                "Breadth of Coverage": {
                    "weight": 0.327,
                    "definition": "Awareness of different possible perspectives related to the topic taught",
                    "example": "Teacher discusses different theoretical views, current and prior scientific developments, etc.",
                    "criteria": {
                        1: "The transcript shows that the instructor covers minimal content with significant gaps in the curriculum",
                        2: "The transcript shows that the instructor covers some content but with notable gaps in the curriculum",
                        3: "The transcript shows that the instructor covers most of the required content with minor gaps",
                        4: "The transcript shows that the instructor covers all required content thoroughly",
                        5: "The transcript shows that the instructor covers all required content and provides additional enrichment material"
                    }
                },
                "Knowledge of Resources": {
                    "weight": 0.310,
                    "definition": "Awareness of and utilization of a variety of current resources in the subject area to enhance instruction",
                    "example": "The teacher cites recent research studies or books while explaining relevant concepts.",
                    "criteria": {
                        1: "The transcript shows that the instructor demonstrates minimal awareness of resources available for teaching",
                        2: "The transcript shows that the instructor demonstrates limited knowledge of resources and rarely incorporates them",
                        3: "The transcript shows that the instructor demonstrates adequate knowledge of resources and sometimes incorporates them",
                        4: "The transcript shows that the instructor demonstrates strong knowledge of resources and frequently incorporates them",
                        5: "The transcript shows that the instructor demonstrates extensive knowledge of resources and consistently incorporates a wide variety of them"
                    }
                }
            }
        },
        "Expository Quality": {
            "weight": 0.179,
            "sub-dimensions": {
                "Content Clarity": {
                    "weight": 0.266,
                    "definition": "Extent to which the teacher is able to explain the content to promote clarity and ease of understanding.",
                    "example": "Teacher uses simple vocabulary and concise sentences to explain complex concepts.",
                    "criteria": {
                        1: "Does not break down complex concepts, uses confusing, imprecise, and inappropriate language, and does not employ any relevant techniques or integrate them into the lesson flow.",
                        2: "Inconsistently breaks down complex concepts using language that is sometimes confusing or inappropriate, employing few minimally relevant techniques that contribute little to student understanding, struggling to integrate them into the lesson flow.",
                        3: "Generally breaks down complex concepts using simple, precise language and some techniques that are somewhat relevant and contribute to student understanding, integrating them into the lesson flow with occasional inconsistencies.",
                        4: "Frequently breaks down complex concepts using simple, precise language and a variety of relevant, engaging techniques that contribute to student understanding.",
                        5: "Consistently breaks down complex concepts using simple, precise language and a wide variety of highly relevant, engaging techniques such as analogies, examples, visuals, etc. to student understanding, seamlessly integrating them into the lesson flow."
                    }
                },
                "Demonstrating Flexibility and Responsiveness": {
                    "weight": 0.248,
                    "definition": "Ability to adapt to the changing needs of the students in the class while explaining the concepts.",
                    "example": "The teacher tries to explain a concept using a particular example. On finding that the students are unable to understand, the teacher is able to produce alternate examples or explanation strategies to clarify the concept.",
                    "criteria": {
                        1: "Fails to adapt explanations based on student needs and does not provide alternate examples or strategies.",
                        2: "Rarely adapts explanations, often sticking to the same methods even when students struggle to understand.",
                        3: "Sometimes adapts explanations and provides alternate examples or strategies, but with limited effectiveness.",
                        4: "Frequently adapts explanations and offers a variety of alternate examples or strategies that aid student understanding.",
                        5: "Consistently and seamlessly adapts explanations, providing a wide range of highly effective alternate examples or strategies tailored to student needs."
                    }
                },
                "Differentiation Strategies": {
                    "weight": 0.246,
                    "definition": "The methods and approaches used by the teacher to accommodate diverse student needs, backgrounds, learning styles, and abilities.",
                    "example": "During a lesson, the teacher divides the class into small groups based on their readiness levels. She provides more advanced problems for students who grasp the concept quickly, while offering additional support and manipulatives for students who need more help.",
                    "criteria": {
                        1: "Uses no differentiation strategies to meet diverse student needs",
                        2: "Uses minimal differentiation strategies with limited effectiveness",
                        3: "Uses some differentiation strategies with moderate effectiveness",
                        4: "Consistently uses a variety of differentiation strategies effectively",
                        5: "Masterfully employs a wide range of differentiation strategies to meet the needs of all learners"
                    }
                },
                "Communication Clarity": {
                    "weight": 0.238,
                    "definition": "The ability of the teacher to effectively convey information and instructions to students in a clear and understandable manner.",
                    "example": "The teachers voice and language is clear with the use of appropriate voice modulation, tone, and pitch to facilitate ease of understanding.",
                    "criteria": {
                        1: "Communicates poorly with students, leading to confusion and misunderstandings",
                        2: "Communicates with some clarity but often lacks precision or coherence",
                        3: "Communicates clearly most of the time, with occasional lapses in clarity",
                        4: "Consistently communicates clearly and effectively with students",
                        5: "Communicates with exceptional clarity, precision, and coherence, ensuring full understanding"
                    }
                }
            }
        },
        "Class Management": {
            "weight": 0.150,
            "sub-dimensions": {
                "Punctuality": {
                    "weight": 0.261,
                    "definition": "The consistency and timeliness of the teacher's arrival to class sessions, meetings, and other professional obligations.",
                    "example": "The teacher starts and completes live lectures as per the designated time.",
                    "criteria": {
                        1: "Transcripts consistently show late class start times and/or early end times",
                        2: "Transcripts occasionally show late class start times and/or early end times",
                        3: "Transcripts usually show on-time class start and end times",
                        4: "Transcripts consistently show on-time class start and end times",
                        5: "Transcripts always show early class start times and full preparation to begin class on time"
                    }
                },
                "Managing Classroom Routines": {
                    "weight": 0.255,
                    "definition": "The Teacher establishes and maintains efficient routines and procedures to maximize instructional time.",
                    "example": "The teacher starts every session with a recap quiz to remind learners of what was taught earlier. Students prepare for the recap even before the teacher enters the class in a habitual manner.",
                    "criteria": {
                        1: "Classroom routines are poorly managed, leading to confusion and lost instructional time",
                        2: "Classroom routines are somewhat managed but with frequent disruptions",
                        3: "Classroom routines are adequately managed with occasional disruptions",
                        4: "Classroom routines are well-managed, leading to smooth transitions and minimal disruptions",
                        5: "Classroom routines are expertly managed, maximizing instructional time and creating a seamless learning environment"
                    }
                },
                "Managing Student Behavior": {
                    "weight": 0.240,
                    "definition": "The teacher sets clear expectations for behavior and uses effective strategies to prevent and address misbehavior. The teacher encourages student participation and provides fair and equal opportunities to all students in class. The teacher also provides appropriate compliments and feedback to learners’ responses.",
                    "example": "The teacher addresses a students misbehavior in the class in a professional manner and provides constructive feedback using clear guidelines for student behavior expected in the course.",
                    "criteria": {
                        1: "Struggles to manage student behavior, leading to frequent disruptions and an unproductive learning environment. Rarely encourages student participation, with little to no effort to ensure equal opportunities for engagement; provides no or inappropriate feedback and compliments that do not support learning or motivation.",
                        2: "Manages student behavior with limited effectiveness, with some disruptions and off-task behavior. Inconsistently encourages student participation, with unequal opportunities for engagement; provides limited or generic feedback and compliments that minimally support learning and motivation.",
                        3: "Manages student behavior adequately, maintaining a generally productive learning environment. Generally encourages student participation and provides opportunities for engagement, but some students may dominate or be overlooked; provides feedback and compliments, but they may not always be specific or constructive.",
                        4: "Effectively manages student behavior, promoting a positive and productive learning environment. Frequently encourages student participation, provides fair opportunities for engagement, and offers appropriate feedback and compliments that support learning and motivation.",
                        5: "Expertly manages student behavior, fostering a highly respectful, engaged, and self-regulated learning community. Consistently encourages active participation from all students, ensures equal opportunities for engagement, and provides specific, timely, and constructive feedback and compliments that enhance learning and motivation."
                    }
                },
                "Adherence to Rules": {
                    "weight": 0.242,
                    "definition": "The extent to which the teacher follows established rules, procedures, and policies governing classroom conduct and professional behavior.",
                    "example": "The teacher reminds the students to not circulate cracked versions of a software on the class discussion forum.",
                    "criteria": {
                        1: "Consistently disregards or violates school rules and policies",
                        2: "Occasionally disregards or violates school rules and policies",
                        3: "Generally adheres to school rules and policies with occasional lapses",
                        4: "Consistently adheres to school rules and policies",
                        5: "Strictly adheres to school rules and policies and actively promotes compliance among students"
                    }
                }
            }
        },
        "Structuring of Objectives and Content": {
            "weight": 0.168,
            "sub-dimensions": {
                "Organization": {
                    "weight": 0.338,
                    "definition": "The extent to which content is presented in a structured and comprehensive manner with emphasis on important content and proper linking content.",
                    "example": "Teacher starts the class by providing an outline of what all will be covered in that particular class and connects it to previous knowledge of learners.",
                    "criteria": {
                        1: "Transcripts indicate content that is poorly organized, with minimal structure and no clear emphasis on important content. Linking between content is absent or confusing.",
                        2: "Transcripts indicate content that is somewhat organized but lacks a consistent structure and comprehensive coverage. Emphasis on important content is inconsistent, and linking between content is weak",
                        3: "Transcripts indicate content that is adequately organized, with a generally clear structure and comprehensive coverage. Important content is usually emphasized, and linking between content is present.",
                        4: "Transcripts indicate content that is well-organized, with a consistent and clear structure and comprehensive coverage. Important content is consistently emphasized, and linking between content is effective.",
                        5: "Transcripts indicate content that is exceptionally well-organized, with a highly structured, logical, and comprehensive presentation. Important content is strategically emphasized, and linking between content is seamless and enhances learning."
                    }
                },
                "Clarity of Instructional Objectives": {
                    "weight": 0.342,
                    "definition": "The clarity and specificity of the learning objectives communicated to students, guiding the focus and direction of instruction.",
                    "example": "At the start of the lesson, the teacher displays the learning objectives and takes a few moments to explain them to the students.",
                    "criteria": {
                        1: "Content is presented in a confusing or unclear manner",
                        2: "Content is presented with some clarity but with frequent gaps or inconsistencies",
                        3: "Content is presented with adequate clarity, allowing for general understanding",
                        4: "Content is presented with consistent clarity, promoting deep understanding",
                        5: "Content is presented with exceptional clarity, facilitating mastery and transfer of knowledge"
                    }
                },
                "Alignment with the Curriculum": {
                    "weight": 0.319,
                    "definition": "The degree to which the teacher's instructional plans and activities align with the prescribed curriculum objectives and standards.",
                    "example": "The teacher discusses a unit plan that clearly shows the connections between her learning objectives, instructional activities, assessments, and the corresponding curriculum standards.",
                    "criteria": {
                        1: "Instruction is poorly aligned with the curriculum, with significant gaps or deviations",
                        2: "Instruction is somewhat aligned with the curriculum but with frequent inconsistencies",
                        3: "Instruction is generally aligned with the curriculum, covering most required content",
                        4: "Instruction is consistently aligned with the curriculum, covering all required content",
                        5: "Instruction is perfectly aligned with the curriculum, covering all required content and providing meaningful extensions"
                    }
                }
            }
        },
        "Qualities of Interaction": {
            "weight": 0.168,
            "sub-dimensions": {
                "Instructor Enthusiasm And Positive demeanor": {
                    "weight": 0.546,
                    "definition": "Extent to which a teacher is enthusiastic and committed to making the course interesting, active, dynamic, humorous, etc.",
                    "example": "Teacher uses an interesting fact or joke to engage the class.",
                    "criteria": {
                        1: "Instructor exhibits a negative or indifferent demeanor and lacks enthusiasm for teaching",
                        2: "Instructor exhibits a neutral demeanor and occasional enthusiasm for teaching",
                        3: "Instructor exhibits a generally positive demeanor and moderate enthusiasm for teaching",
                        4: "Instructor exhibits a consistently positive demeanor and strong enthusiasm for teaching",
                        5: "Instructor exhibits an exceptionally positive demeanor and infectious enthusiasm for teaching, inspiring student engagement"
                    }
                },
                "Individual Rapport": {
                    "weight": 0.453,
                    "definition": "Extent to which the teacher develops a rapport with individual students and their concerns during and beyond class hours. The teacher provides assistance, guidance, and resources to help students overcome obstacles, address challenges, and achieve success.",
                    "example": "Teacher shows an interest in student concerns, and attempts to resolve individual queries both during the class and through forums/individual communication.",
                    "criteria": {
                        1: "Minimal or negative rapport with individual students interactions",
                        2: "Limited rapport with individual students, with infrequent personalized",
                        3: "Adequate rapport with individual students, with some personalized interactions",
                        4: "Strong rapport with individual students, with frequent personalized interactions and support",
                        5: "Exceptional rapport with each individual student, with highly personalized interactions, support, and guidance"
                    }
                }
            }
        },
        "Evaluation of Learning": {
            "weight": 0.163,
            "sub-dimensions": {
                "Course Level Assessment": {
                    "weight": 0.333,
                    "definition": "The course level assessment is in line with the curriculum of the course and effectively checks whether the course outcomes are being met.",
                    "example": "The teacher selects or uses test items that reflect the course outcome.",
                    "criteria": {
                        1: "The course level assessment is not aligned with the curriculum, does not cover course outcomes, and uses methods that are ineffective in measuring student achievement of these outcomes.",
                        2: "The course level assessment is poorly aligned with the curriculum, covers few course outcomes, and uses methods that are limited in their ability to effectively measure student achievement of these outcomes.",
                        3: "The course level assessment is generally aligned with the curriculum, covers some course outcomes, and uses methods that adequately measure student achievement of these outcomes, but may have minor gaps or inconsistencies.",
                        4: "The course level assessment is well-aligned with the curriculum, covers most course outcomes, and uses appropriate methods to effectively measure student achievement of these outcomes.",
                        5: "The course level assessment is perfectly aligned with the curriculum, comprehensively covers all course outcomes, and employs highly effective methods to accurately measure student achievement of these outcomes."
                    }
                },
                "Clear Grading Criteria": {
                    "weight": 0.333,
                    "definition": "The teacher uses a clear and structured rubric which is communicated to the learners prior to any evaluation. The teacher is not biased in their assessment of learner performance.",
                    "example": "The teacher discusses the assessment rubric by providing examples of good responses and the criteria for grading with the learners before conducting any tests.",
                    "criteria": {
                        1: "The teacher rarely or never uses a rubric, does not communicate assessment criteria to learners before evaluation, and the teacher's assessment is highly biased and unfair.",
                        2: "The teacher inconsistently uses a rubric that is poorly structured or not clearly communicated to learners before evaluation, and the teacher's assessment may be noticeably biased at times.",
                        3: "The teacher generally uses a rubric that is communicated to learners before evaluation, but the rubric may lack some clarity or structure, and the teacher's assessment may occasionally show minor bias.",
                        4: "The teacher frequently uses a clear and structured rubric that is communicated to learners prior to evaluation, and applies the rubric fairly to all learners with minimal bias.",
                        5: "The teacher consistently uses a well-defined, comprehensive rubric that is clearly communicated to learners well in advance of any evaluation, and applies the rubric objectively and fairly to all learners without any bias."
                    }
                },
                "Assignments/readings": {
                    "weight": 0.332,
                    "definition": "The teacher provides assignments/homework/literature which is relevant and contributes to a deeper understanding of the topics taught to track the progress of learners. The teacher also discusses the solutions and feedback based on previously assigned homework/assignment.",
                    "example": "The teacher provides clear instructions on the homework task that the students are given and how it is relevant to the topics taught in class. In the following class, the teacher discusses the answers and any common mistakes made by learners.",
                    "criteria": {
                        1: "The teacher rarely or never provides relevant assignments, homework, or literature that contribute to understanding the topics taught, does not track learner progress, and fails to discuss solutions and feedback based on previous work.",
                        2: "The teacher inconsistently provides assignments, homework, and literature that are minimally relevant and contribute little to understanding the topics taught, rarely tracks learner progress, and seldom discusses solutions and feedback based on previous work.",
                        3: "The teacher generally provides assignments, homework, and literature that are somewhat relevant and contribute to understanding the topics taught, occasionally tracks learner progress, and sometimes discusses solutions and feedback based on previous work.",
                        4: "The teacher frequently provides relevant assignments, homework, and literature that contribute to a deeper understanding of the topics taught, tracks learner progress, and discusses solutions and feedback based on previously assigned work.",
                        5: "The teacher consistently provides highly relevant and challenging assignments, homework, and literature that significantly deepen learners' understanding of the topics taught, regularly tracks learner progress, and engages in thorough discussions of solutions and feedback based on previous work."
                    }
                }
            }
        }
    
    }
