CREATE TABLE schools(
    school VARCHAR(100) PRIMARY KEY,
    school_count INT,
    repeat_faculty INT,
    unique_faculty INT
);

INSERT INTO schools(school, school_count) 
VALUES 
('College of Arts & Sciences', 45),
('School of Nursing', 23),
('Kenan-Flagler Business School', 10),
('School of Education', 8),
('Hussman School of Journalism and Media', 4),
('School of Government', 2),
('School of Medicine', 2),
('Gillings School of Global Public Health', 2);

CREATE TABLE departments(
    department VARCHAR(100),
    course VARCHAR(100)
);

INSERT INTO departments(department, course) VALUES
('Geography', 'GEOG 435'),
('Geography', 'GEOG 803'),
('Geography', 'GEOG 457'),
('Education', 'EDMX 716'),
('Education', 'EDMX 710'),
('Education', 'EDUC 475'),
('Education', 'EDUC 526'),
('Education', 'EDUC 615'),
('Education', 'EDUC 375'),
('Middle Eastern and Asian Studies', 'JAPN 401'),
('Middle Eastern and Asian Studies', 'CHIN 101'),
('Middle Eastern and Asian Studies', 'CHIN 407'),
('Middle Eastern and Asian Studies', 'CHIN 102'),
('Middle Eastern and Asian Studies', 'CHIN 305'),
('Middle Eastern and Asian Studies', 'CHIN 443'),
('Middle Eastern and Asian Studies', 'CHIN 306'),
('Middle Eastern and Asian Studies', 'ASIA 231'),
('Middle Eastern and Asian Studies', 'ASIA 721'),
('Middle Eastern and Asian Studies', 'ASIA/CMPL 127'),
('Middle Eastern and Asian Studies', 'ASIA 69'),
('Romance Studies', 'SPAN 329'),
('Romance Studies', 'SPAN 344'),
('Romance Studies', 'FREN 150'),
('Anthropology', 'FOLK/ANTH 424'),
('Anthropology', 'ANTH 442'),
('Anthropology', 'ANTH 190'),
('Nursing', 'NURS 934'),
('Nursing', 'NURS 402'),
('Nursing', 'NURS 483'),
('Nursing', 'NURS 482'),
('Nursing', 'NURS 740'),
('Nursing', 'NURS 691'),
('Nursing', 'NURS 746'),
('Nursing', 'NURS 301'),
('Nursing', 'NURS 864'),
('Nursing', 'NURS 320'),
('Nursing', 'NURS 402C'),
('American Studies', 'HIST 783'),
('American Studies', 'HIST 140'),
('American Studies', 'AAAD 320'),
('African, African American, and Diaspora Studies', 'FOLK/ANTH 424'),
('Business', 'BUSI 206'),
('Business', 'BUSI 201'),
('Business', 'BUSI 529'),
('Business', 'BUSI 301'),
('History', 'HIST 783'),
('History', 'HIST 140'),
('Public Health Leadership', 'PUBH 730'),
('Public Health Leadership', 'HBEH 784'),
('Public Health Leadership', 'MHCH 728'),
('Germanic and Slavic Languages and Literatures', 'RUSS 515'),
('Germanic and Slavic Languages and Literatures', 'RUSS 516'),
('Journalism', 'MEJO 531'),
('Journalism', 'MEJO 560'),
('Journalism', 'MEJO 553'),
('Allied Health Sciences', 'NURS 483'),
('Allied Health Sciences', 'NURS 402'),
('Department of Public Health Leadership and Practice', 'PUBH 730'),
('Human Development & Family Science', 'SPHS 751'),
('Peace, War, and Defense', 'PWAD 490'),
('Peace, War, and Defense', 'DRAM 284'),
('Health Behavior', 'BUSI 529'),
('English & Comparative Literature', 'ENGL 494'),
('English & Comparative Literature', 'ENGL 266'),
('English & Comparative Literature', 'ENGL 118'),
('English & Comparative Literature', 'ENGL 763'),
('Department of Environmental Sciences and Engineering', 'ENVR 548'),
('Music', 'MUSC 214'),
('Music', 'MUSC 105'),
('Psychology', 'PSYC 751'),
('Classics', 'CLAS 363H'),
('Asian and Middle Eastern Studies', 'CHIN 101'),
('Government', 'POLI 290'),
('Government', 'POLI 438'),
('Art & Art History', 'ARTS 322'),
('Political Science', 'POLI 290'),
('Political Science', 'POLI 438'),
('Dramatic Art', 'DRAM 284');