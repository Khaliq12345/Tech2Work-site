export function useContactPeople() {
  const people = [
    {
      name: "Khaliq Salawou",
      role: "Full-Stack Dev",
      linkedin: "https://www.linkedin.com/in/khaliq-salawou-b2a90a22b/",
    },
    {
      name: "Natalia Zamai",
      role: "Data Engineer",
      image: "https://randomuser.me/api/portraits/women/44.jpg",
      linkedin: "https://linkedin.com/in/natalia",
    },
  ];
  return {
    people,
  };
}

