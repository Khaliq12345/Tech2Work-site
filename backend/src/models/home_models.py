from sqlmodel import JSON, SQLModel, Field
from src.core.config import ENGINE
from src.utils import get_session

class HomeService(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    classname: str
    title: str
    description: str
    icon: str
    features: list[str] = Field(sa_type=JSON)

class HomeTestimonial(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    classname: str
    quote: str
    name: str
    role: str
    avatar: str
    
class ServiceTechStack(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    classname: str
    title: str
    desc: str
    icon: str
    type: str # 'service' | 'techstack'
    
class HomeIndustry(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    icon: str
    description: str
    samples: list[str] = Field(sa_type=JSON)
    
class HomeProcess(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str

class FAQ(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    label: str
    content: str

def create_table():
    SQLModel.metadata.create_all(ENGINE)

def clear_all():
    pass
    # with get_session() as session:
    #     for table in reversed(SQLModel.metadata.sorted_tables):
    #         stmt = select(table)
    #         results = session.exec(stmt).all()
    #         for obj in results:
    #             session.delete(obj)
    #     session.commit()
    # SQLModel.metadata.drop_all(ENGINE)
    
async def bind_all():
    await bind_faq()
    await bind_service_tech_stack()

async def bind_faq():
     with get_session() as session:
        items = [
            FAQ(
                label="What are the key features I should consider in custom healthcare software?",
                content="Our custom medical software development company guarantees high-quality products and on-time releases. Here’s how we deliver exceptional value:",
            ),
            FAQ(
                label="How much does custom healthcare software development cost?",
                content="We offer a variety of engagement models to suit your budget and project timeframe. This ensures cost-effectiveness and timely delivery of custom healthcare software development services without compromising on quality.",
            ),
            FAQ(
                label="What about integrating custom healthcare software with existing systems?",
                content="Our experienced team utilizes industry best practices for project management. We employ an iterative custom healthcare application software development approach, ensuring regular progress updates with on-time demos to foster clear communication throughout the development lifecycle.",
            ),
            FAQ(
                label="How can I find a reputable custom healthcare software development company?",
                content="Our team goes beyond just software development: we have a team of healthcare professionals and software developers who understand the unique needs of the healthcare industry. This combined expertise allows us to offer advanced custom healthcare software design and development that perfectly align with your requirements.",
            ),
            FAQ(
                label="What are some of the challenges associated with custom healthcare software development?",
                content="Custom healthcare software development comes with its own set of challenges, but with careful planning and a skilled development team, these hurdles can be overcome:\nStrict regulations and the ever-present threat of cyberattacks necessitate robust security measures throughout the development process.\nWorking with a development team familiar with HIPAA and other relevant regulations helps ensure your software meets compliance standards.\nClear communication with stakeholders and an agile development methodology allow for adapting to changing requirements throughout the development process.",
            ),
        ]
        for item in items:
            session.add(item)
        session.commit()

async def bind_service_tech_stack():
     with get_session() as session:
        items = [
            ServiceTechStack(
                classname="text-white bg-gradient-to-br from-black to-gray-400",
                title="Product Development",
                desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
                icon="i-lucide-mail",
                type="service",
            ),
            ServiceTechStack(
                classname="flex-2/4 text-white bg-gradient-to-br from-black to-gray-400",
                title="Product Development",
                desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
                icon="i-lucide-mail",
                type="service",
            ),
            ServiceTechStack(
                classname="flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
                title="Product Development",
                desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
                icon="i-lucide-mail",
                type="service",
            ),
            ServiceTechStack(
                classname="flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
                title="Product Development",
                desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
                icon="i-lucide-mail",
                type="service",
            ),
            ServiceTechStack(
                classname="flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
                title="Product Development",
                desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
                icon="i-lucide-mail",
                type="techstack",
            ),
            ServiceTechStack(
                classname="flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
                title="Product Development",
                desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
                icon="i-lucide-mail",
                type="techstack",
            ),
            ServiceTechStack(
                classname="flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
                title="Product Development",
                desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
                icon="i-lucide-mail",
                type="techstack",
            ),
            ServiceTechStack(
                classname="flex-1/4 text-white bg-gradient-to-br from-black to-gray-400",
                title="Product Development",
                desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
                icon="i-lucide-mail",
                type="techstack",
            ),
            ServiceTechStack(
                classname="flex-2/4 text-white bg-gradient-to-br from-black to-gray-400",
                title="Product Development",
                desc="Have a product idea but no technical team? We help you define the need, shape the vision, and deliver a complete software solution.",
                icon="i-lucide-mail",
                type="techstack",
            ),
        ]
        for item in items:
            session.add(item)
        session.commit()


