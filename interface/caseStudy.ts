export interface CaseStudy {
    id: string;
    clientLogo: string; 
    title: string;
    description: string;
    location: string;
    technologies: string[];
    clientStory: string;
    businessNeed: string[]; 
    mediaUrl: string,
    mediaType: 'image' | 'video'; 
}