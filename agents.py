from crewai import Agent



#senior blog-agent

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video content for the topic{topic} from youtube'
)