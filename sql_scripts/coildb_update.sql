--
-- PostgreSQL database dump
--

-- Dumped from database version 17.0
-- Dumped by pg_dump version 17.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: faculty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faculty (
    "Last Name" character varying(100) NOT NULL,
    "First Name" character varying(100) NOT NULL,
    "Email" character varying(100) NOT NULL,
    "Semester Taught" character varying(100) NOT NULL,
    "School" character varying(500),
    "Department" character varying(500),
    "Course Name" character varying(100),
    "Course Number" character varying(100),
    "Sections" character varying(100),
    "Total # Sections Taught" integer,
    "Course Title" character varying(500) NOT NULL,
    "Co-taught Semester" character varying(100),
    "Co-taught Year" integer,
    "Repeat Course Semester" character varying(100),
    "Repeat Course Year" integer,
    "Joint - course" character varying,
    "Quarter" character varying(100),
    "Estimated UNC Students " integer,
    "Estimated Partner Students" integer,
    "Enrolled UNC Students (FDOC)" integer,
    "Enrolled UNC Students (LDOC)" integer,
    "Partner Institution 1" character varying(500),
    "Partner Country 1" character varying(100),
    "Partner Faculty 1" character varying(100),
    "Partner Institution 2" character varying(100),
    "Partner Country 2" character varying(100),
    "Partner Faculty 2" character varying(100),
    "EE/HI Credit" character varying(100),
    "Award Date" date,
    "Graduate Student" character varying(100),
    "Faculty Amount Awarded" integer,
    "Graduate Student Award Amount " integer,
    "Repeat Award " character varying(100),
    "Repeat Award Criteria " character varying(100),
    "COIL Champion" character varying(100),
    "Notes" character varying(1500),
    "Partner region" character varying(50),
    "Cancelled" boolean NOT NULL
);


ALTER TABLE public.faculty OWNER TO postgres;

--
-- Name: grad_student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.grad_student (
    "Semester Taught" character varying(100) NOT NULL,
    "Year Taught" integer NOT NULL,
    "Last Name" character varying(100) NOT NULL,
    "First Name" character varying(100) NOT NULL,
    "Faculty Supervisor" character varying(100),
    "School" character varying(100),
    "Department" character varying(100),
    "Course" character varying(50) NOT NULL,
    "Number" character varying(50) NOT NULL,
    "UNC Course Name" character varying(100),
    "Partner Institution" character varying(100),
    "Award" integer,
    "TA Email" character varying(100),
    "TA PID" integer
);


ALTER TABLE public.grad_student OWNER TO postgres;

--
-- Data for Name: faculty; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.faculty ("Last Name", "First Name", "Email", "Semester Taught", "School", "Department", "Course Name", "Course Number", "Sections", "Total # Sections Taught", "Course Title", "Co-taught Semester", "Co-taught Year", "Repeat Course Semester", "Repeat Course Year", "Joint - course", "Quarter", "Estimated UNC Students ", "Estimated Partner Students", "Enrolled UNC Students (FDOC)", "Enrolled UNC Students (LDOC)", "Partner Institution 1", "Partner Country 1", "Partner Faculty 1", "Partner Institution 2", "Partner Country 2", "Partner Faculty 2", "EE/HI Credit", "Award Date", "Graduate Student", "Faculty Amount Awarded", "Graduate Student Award Amount ", "Repeat Award ", "Repeat Award Criteria ", "COIL Champion", "Notes", "Partner region", "Cancelled") FROM stdin;
Allred	Shorna	shorna@unc.edu 	Summer 2024	College of Arts & Sciences	Geography	GEOG	435	1	1	Global Environmental Justice	\N	\N	Summer	2024	\N	Summer I	10	27	4	4	Universitas\tMulawarman	Indonesia	Rustam Fahmy	\N	\N	\N	\N	2024-05-24	requested	2500	\N	 Yes 	 Same course same partner 	\N	didn't find grad student	Asia	f
Allred	Shorna	shorna@unc.edu 	Spring 2024	College of Arts & Sciences	Geography	GEOG	435	1	1	Global Environmental Justice	\N	\N	\N	\N	\N	\N	28	10	28	28	Universitas\tMulawarman	Indonesia	Rustam\tFahmy and Emi\tPurwanti	\N	\N	\N	\N	2024-11-23	requested	2500	\N	\N	\N	\N	didn't find grad student	Asia	f
Amsbary	Jessica	amsbary@email.unc.edu 	Fall 2022	School of Education	Education	EDMX	716	1	1	Early Childhood Assessment and Differentiation	\N	\N	\N	\N	\N	\N	20	20	20	19	National Institute of Education at the Nanyang Technological University (NIE-NTU)	Singapore	Huichao Xie	\N	\N	\N	\N	2024-04-22	1	1250	1500	\N	\N	\N	co-taught w/Chih-ing Lim	Asia	f
Amsbary	Jessica	amsbary@email.unc.edu	Spring 2025	School of Education	Education	EDMX	710	1	1	Early Childhood Leadership	\N	\N	\N	\N	\N	\N	20	20	\N	\N	University College Dublin	Ireland	Huichao Xie	\N	\N	\N	\N	2024-05-24	requested	1250	\N	\N	\N	\N	co-taught w/Chih-ing Lim	Europe	f
Aratake	Yuki	yaratake@email.unc.edu	Fall 2024	College of Arts & Sciences	Middle Eastern and Asian Studies	JAPN	401	1	1	Gateway to Mastering Japanese	\N	\N	Fall	2024	\N	\N	12	15	\N	\N	Hokkaido Musashi Women's Junior College	Japan	Hatsuko Itaya	\N	\N	\N	\N	2024-11-23	no	2500	\N	Yes	Same course same partner	\N	\N	Asia	f
Aratake	Yuki	yaratake@email.unc.edu	Fall 2023	College of Arts & Sciences	Middle Eastern and Asian Studies	JAPN	401	1	1	Gateway to Mastering Japanese	\N	\N	\N	\N	\N	\N	12	15	\N	18	Hokkaido Musashi Women's Junior College	Japan	Hatsuko Itaya	\N	\N	\N	\N	2024-11-22	no	2500	\N	\N	\N	\N	\N	Asia	f
Aviles de Leon	Lornaida	avilesl@email.unc.edu	Spring 2021	College of Arts & Sciences	Romance Studies	SPAN	329	1	1	Spanish for Professional & Community Engagement	\N	\N	\N	\N	\N	\N	8	8	10	10	Universidad San Francisco de Quito	Ecuador	Esteban Mayorga	\N	\N	\N	\N	2024-10-20	no	2500	\N	\N	\N	\N	\N	Latin America	f
Babb	Florence	fbabb@unc.edu	Fall 2022	College of Arts & Sciences	Anthropology	LTAM	101	1	1	Introduction to Latin American Studies	\N	\N	Fall	2022	\N	\N	22	22	21	19	Universidad San Francisco de Quito	Ecuador	Michael Hill	\N	\N	\N	\N	2024-12-21	2	2500	1500	 Yes 	 Same course same partner 	\N	Split with 2 grad students	Latin America	f
Babb	Florence	fbabb@unc.edu	Fall 2023	College of Arts & Sciences	Anthropology	LTAM	101	1	1	Introduction to Latin American Studies	\N	\N	Fall	2023	\N	\N	22	20	\N	17	Universidad San Francisco de Quito	Ecuador	Dayuma Alban	\N	\N	\N	\N	2024-05-23	1	2500	1500	 Yes 	 Same course same partner 	\N	\N	Latin America	f
Babb	Florence	fbabb@unc.edu	Fall 2021	College of Arts & Sciences	Anthropology	LTAM	101	1	1	Introduction to Latin American Studies	\N	\N	\N	\N	\N	\N	25	20	23	22	Universidad San Francisco de Quito	Ecuador	Michael Hill	\N	\N	\N	\N	2024-03-21	2	2500	1500	\N	\N	\N	Split with 2 grad students	Latin America	f
Baker	Maureen	mjbaker@ad.unc.edu	Fall 2022	School of Nursing	Nursing	NURS	934	1	1	Clinical Scholarship and Professional Communication	\N	\N	Fall	2022	\N	\N	17	16	17	17	St. Luke's International University	Japan	Erika Ota	\N	\N	\N	\N	2024-10-21	1	2500	1500	 Yes 	 Same course same partner 	\N	\N	Asia	f
Baker	Maureen	mjbaker@ad.unc.edu	Fall 2023	School of Nursing	Nursing	NURS	934	1	1	Clinical Scholarship and Professional Communication	\N	\N	Fall	2023	\N	\N	18	14	\N	6	St. Luke's International University	Japan	Erika Ota	\N	\N	\N	\N	2024-06-23	1	2500	1500	 Yes 	 Same course same partner 	\N	\N	Asia	f
Baker	Maureen	mjbaker@ad.unc.edu	Fall 2021	School of Nursing	Nursing	NURS	934	1	1	Clinical Scholarship and Professional Communication	\N	\N	\N	\N	\N	\N	19	16	17	16	St. Luke's International University	Japan	Erika Ota	\N	\N	\N	\N	2024-03-21	1	2500	1500	\N	\N	\N	\N	Asia	f
Berlinger	Gabrielle	gberling@unc.edu	Spring 2023	College of Arts & Sciences	American Studies	FOLK/ANTH	424	1	1	Ritual / Festival / Public Culture	\N	\N	\N	\N	\N	\N	45	25	25	24	University College Dublin	Ireland	Tiber Falzett	\N	\N	\N	\N	2024-04-22	1	2500	1500	\N	\N	\N	\N	Europe	f
Birya	Raphael	rbirya@email.unc.edu	Fall 2023	College of Arts & Sciences	 African African American and Diaspora Studies	SWAH	403	\N	1	Intermediate Kiswahili III	\N	\N	\N	\N	\N	\N	10	10	\N	12	Pwani University	Kenya	Nancy Ngowa	\N	\N	\N	\N	2024-06-23	1	2500	1500	 Yes 	\N	\N	\N	Africa	f
Birya	Raphael	rbirya@email.unc.edu	Spring 2023	College of Arts & Sciences	 African African American and Diaspora Studies	SWAH	402	\N	1	Elementary Kiswahili II	\N	\N	\N	\N	\N	\N	15	15	14	14	Pwani University	Kenya	Nancy Ngowa	\N	\N	\N	\N	2024-11-22	1	2500	1500	\N	\N	\N	\N	Africa	f
Birya	Raphael	rbirya@email.unc.edu	Spring 2024	College of Arts & Sciences	 African African American and Diaspora Studies	SWAH	402	\N	1	Elementary Kiswahili II	\N	\N	Spring	2024	\N	\N	15	15	13	13	Pwani University	Kenya	Nancy Ngowa	\N	\N	\N	\N	2024-11-23	1	2500	1500	 Yes 	\N	\N	\N	Africa	f
Birya	Raphael	rbirya@email.unc.edu	Fall 2024	College of Arts & Sciences	 African African American and Diaspora Studies	SWAH	403	1	1	Intermediate Kiswahili III	\N	\N	Fall	2024	\N	\N	15	15	\N	\N	Pwani University	Kenya	Nancy Ngowa	\N	\N	\N	\N	2024-05-24	requested	1500	\N	 Yes 	\N	 Fall 2024 	COIL Champion	Africa	f
Bond	David	David_bond@kenan-flagler.unc.edu 	Spring 2021	Kenan-Flagler Business School	Business	BUSI	206	\N	1	Business in Africa	\N	\N	\N	\N	\N	Q1	25	25	11	11	University of Stellenbosch	South Africa	Marjolijn Dijksterhuis	\N	\N	\N	\N	2024-06-20	requested	3000	\N	\N	\N	\N	\N	Africa	f
Bond	David	David_bond@kenan-flagler.unc.edu 	Summer 2022	Kenan-Flagler Business School	Business	BUSI	201	\N	1	Business in Europe - Leadership and Innovation for Positive Global Change	\N	\N	\N	\N	\N	Summer I	30	15	30	30	Erasmus University	The Netherlands	Eva Rood	\N	\N	\N	\N	2024-04-22	requested	2500	\N	\N	\N	\N	Positive Change Initiative Rotterdam School of Management	Europe	f
Bonilla	Evi	ebonilla@unc.edu	Spring 2023	School of Nursing	Nursing	NURS	402	\N	1	Foundations of Population Health and Global Health: Carolina Core IV	\N	\N	\N	\N	\N	\N	110	40	102	102	Australian Catholic University	Australia	\N	\N	\N	\N	\N	2024-11-22	1	2500	1500	\N	\N	\N	\N	Oceania	f
Bryant	Chad	bryantc@email.unc.edu	Fall 2024	College of Arts & Sciences	History	HIST	783	\N	1	Readings in East European History	\N	\N	Fall	2024	\N	\N	12	6	\N	\N	Charles University	Czechia	Ota Konrad	\N	\N	\N	\N	2024-05-24	\N	2500	\N	 Yes 	\N	\N	\N	Europe	f
Bryant	Chad	bryantc@email.unc.edu	Fall 2022	College of Arts & Sciences	History	HIST	783	\N	1	Readings in Russian and East European History	\N	\N	Fall	2022	\N	\N	11	9	15	15	King's College London	England	James Bjork	Charles University	Czechia	Ota Konrad	\N	2024-10-21	1	2500	1500	 Yes 	\N	\N	\N	Europe	f
Bryant	Chad	bryantc@email.unc.edu	Spring 2021	College of Arts & Sciences	History	HIST	783	\N	1	Readings in Russian and East European History	\N	\N	\N	\N	\N	\N	8	8	9	9	King's College London	England	Uta Balabier	Charles University	Czechia	Ota Konrad	\N	2024-10-20	1	2500	1500	\N	\N	\N	\N	Europe	f
Cai	Luoyi	luoyicai@email.unc.edu	Fall 2022	College of Arts & Sciences	Middle Eastern and Asian Studies	CHIN	101	2 3 4 and 5	4	Elementary Chinese I	\N	\N	\N	\N	\N	\N	60	5	57	57	Beijing Normal University	China	Hang Ke	\N	\N	\N	\N	2024-07-22	no	2500	\N	\N	\N	\N	\N	Asia	f
Cai	Luoyi	luoyicai@email.unc.edu	Fall 2023	College of Arts & Sciences	Middle Eastern and Asian Studies	CHIN	407	\N	1	Readings in Chinese I	\N	\N	\N	\N	\N	\N	18	6	\N	20	Beijing Language and Culture University	China	Ting Wen	\N	\N	\N	\N	2024-07-23	no	2500	\N	\N	\N	\N	\N	Asia	f
Cai	Luoyi	luoyicai@email.unc.edu	Spring 2023	College of Arts & Sciences	Middle Eastern and Asian Studies	CHIN	102	2 and 4	2	Elementary Chinese II	\N	\N	\N	\N	\N	\N	40	4	45	45	Beijing Normal University	China	Hang Ke	\N	\N	\N	\N	2024-12-22	no	2500	\N	Yes	\N	\N	\N	Asia	f
Cannon	Sharon	Sharon_Cannon@kenan-flagler.unc.edu	Fall 2021	Kenan-Flagler Business School	Business	BUSI	529	1	1	Intercultural Communication for the Global Workplace	\N	\N	Fall	2021	\N	\N	25	25	26	23	Sophia University	Japan	Gavin Furukawa	\N	\N	\N	\N	2024-05-21	no	2500	\N	 Yes 	\N	\N	\N	Asia	f
Cannon	Sharon	Sharon_Cannon@kenan-flagler.unc.edu	Spring 2021	Kenan-Flagler Business School	Business	BUSI	529	1	1	Intercultural Communication for the Global Workplace	\N	\N	\N	\N	\N	Q2	20	20	25	19	Sophia University	Japan	Gavin Furukawa	\N	\N	\N	\N	2024-06-20	no	2000	\N	\N	\N	\N	rest of award from ACE ($1k)	Asia	f
Chandler	Caroline	chandlec@live.unc.edu	Spring 2025	Gillings School of Global Public Health	Public Health Leadership	MHCH	728	\N	\N	Implementation Research and Practice in Maternal Child and Family Health	\N	\N	\N	\N	\N	\N	40	20	\N	\N	National University of Singapore	Singapore	Yoke Hwee Chan	KK Women's and Children's Hosptial	Singapore	Kerry Chan & Fabian Yap	\N	2024-11-23	\N	850	\N	\N	\N	\N	Co-developed with Oscar Flemming and Minzhi Xing	Asia	f
Chernysheva	Natalia	chernysn@email.unc.edu 	Fall 2022	College of Arts & Sciences	Germanic and Slavic Languages and Literatures	RUSS	515	\N	1	Oral and Professional Communication in Russian	\N	\N	\N	\N	\N	\N	10	10	19	21	Yerevan State University	Armenia	Dr. Alexander Markarov	\N	\N	\N	\N	2024-04-22	requested	2500	\N	\N	\N	\N	didn't find grad student	CSEEES	f
Chernysheva	Natalia	chernysn@email.unc.edu	Spring 2023	College of Arts & Sciences	Germanic and Slavic Languages and Literatures	RUSS	516	\N	1	Advanced Russian Communication Composition and Grammar in the Professions	\N	\N	\N	\N	\N	\N	20	20	10	10	Yerevan State University	Armenia	Dr. Alexander Markarov	\N	\N	\N	\N	2024-11-22	no	2500	\N	Yes?	\N	\N	\N	CSEEES	f
Cosgrove	Beth	beth11@email.unc.edu	Fall 2024	School of Nursing	Nursing	NURS	483	\N	\N	Family Centered Nursing Care from Birth through Adolescence	Fall	2024	\N	\N	\N	\N	0	0	0	0	Universidade de São Paulo	Brazil	Maiara Rodrigues dos Santos	\N	\N	\N	\N	2024-05-24	\N	1000	\N	Yes	COIL Champion	Fall 2024	co-taught with Lisa Woodley	Latin America	f
Cosgrove	Beth	beth11@email.unc.edu	Fall 2023	School of Nursing	Nursing	NURS	483	\N	\N	Family Centered Nursing Care from Birth through Adolescence	Fall	2023	\N	\N	\N	\N	0	0	0	0	Universidade de São Paulo	Brazil	Maiara Rodrigues dos Santos	\N	\N	\N	\N	2024-08-23	1	1250	1500	\N	\N	\N	co-taught with Lisa Woodley	Latin America	f
Cosgrove	Beth	beth11@email.unc.edu	Spring 2024	School of Nursing	Nursing	NURS	483	\N	\N	Family Centered Nursing Care from Birth through Adolescence	Spring	2024	\N	\N	\N	\N	0	0	0	0	Universidade de São Paulo	Brazil	Maiara Rodrigues dos Santos	\N	\N	\N	\N	2024-11-23	1	1250	1500	Yes	\N	\N	co-taught with Lisa Woodley	Latin America	f
Cosgrove	Beth	beth11@email.unc.edu	Spring 2023	School of Nursing	Nursing	NURS	483	\N	1	Family Centered Nursing Care from Birth through Adolescence	\N	\N	Spring	2023	\N	\N	100	40	102	102	Universidade de São Paulo	Brazil	Maiara Rodrigues dos Santos	\N	\N	\N	\N	2024-11-22	1	2500	1500	\N	\N	\N	While this was Beth's first time teaching the course it is a repeat course (not award) with the same UNC course and same partner	Latin America	f
Crawford	Cathy	cmcrawfo@email.unc.edu	Fall 2023	School of Nursing	Nursing	NURS	482	\N	\N	Reproductive Health and the Nursing Care of the Childbearing Family	Fall	2023	\N	\N	\N	\N	0	0	0	0	Western Norway University of Applied Sciences	Norway	Elisabeth Hemnes Aanensen	\N	\N	\N	\N	2024-05-23	requested - co w/Rhonda	1250	\N	\N	\N	\N	Co-taught with Rhonda Lanning.	Europe	f
Crawford	Cathy	cmcrawfo@email.unc.edu	Spring 2024	School of Nursing	Nursing	NURS	482	\N	\N	Reproductive Health and the Nursing Care of the Childbearing Family	Spring	2024	\N	\N	\N	\N	0	0	0	0	Western Norway University of Applied Sciences	Norway	Elisabeth Hemnes Aanensen	\N	\N	\N	\N	2024-01-24	no	1250	\N	\N	\N	\N	Co-taught with Rhonda Lanning.	Europe	f
Czabovsky	Joseph	cabosky@live.unc.edu	Fall 2022	Hussman School of Journalism and Media	Journalism	MEJO	531	3	1	Case Studies in Public Relations	\N	\N	\N	\N	\N	\N	25	15	30	30	Pontificia Universidad Católica de Chile	Chile	Claudia Labarca Encina	\N	\N	\N	\N	2024-03-21	1	2500	1500	\N	\N	\N	First name is now Lightning	Latin America	f
Davis	Leslie	lldavis@email.unc.edu	Spring 2022	School of Nursing	Nursing	NURS	740	1	1	Evidence-based Practice and Research	\N	\N	\N	\N	\N	\N	85	15	23	23	Chiang Mai University	Thailand	Patraporn Tungpunkom	\N	\N	\N	\N	2024-03-21	1	1250	1500	\N	\N	\N	co-taught w/Elizabeth Walters. (23 DNP involved in COIL not whole class)	Asia	f
Domby	Lisa	Lisa_Domby@med.unc.edu	Spring 2023	School of Medicine	Allied Health Sciences	SPHS	751	\N	1	Global Issues and Practices in Communication Sciences and Disorders	\N	\N	Spring	2023	\N	\N	25	25	5	5	Universidad Rafael Landivar	Guatemala	Guicela Ramirez	\N	\N	\N	\N	2024-11-22	1	2500	1500	 Yes 	\N	\N	\N	Latin America	f
Domby	Lisa	Lisa_Domby@med.unc.edu	Spring 2024	School of Medicine	Allied Health Sciences	SPHS	751	\N	1	Global Issues and Practices in Communication Sciences and Disorders	\N	\N	Spring	2024	\N	\N	25	25	9	9	Universidad Rafael Landivar	Guatemala	Guicela Ramirez	\N	\N	\N	\N	2024-06-23	1	2500	1500	 Yes 	\N	\N	\N	Latin America	f
Domby	Lisa	lisa_domby@med.unc.edu	Spring 2022	School of Medicine	Allied Health Sciences	SPHS	751	1	1	Global Issues and Practices in Communication Sciences and Disorders	\N	\N	\N	\N	\N	\N	25	25	16	16	Universidad Rafael Landivar	Guatemala	Mariela España	\N	\N	\N	\N	2024-10-21	1	2500	1500	\N	\N	\N	\N	Latin America	f
Excellent	Marie Lina	marilina@live.unc.edu	Spring 2025	Gillings School of Public Health	Department of Public Health Leadership and Practice	PUBH	730	\N	1	Leading Continuous Quality Improvement (CQI) in Public Health 	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Manipal Academy of Higher Education	India	Dr. Sindhura Lakshimi	\N	\N	\N	\N	2024-05-24	\N	2500	\N	\N	\N	\N	\N	Asia	f
Fleming	Oscar	oscar.fleming@unc.edu	Spring 2025	Gillings School of Global Public Health	Public Health Leadership	MHCH	728	\N	0	Implementation Research and Practice in Maternal Child and Family Health	Spring	2025	\N	\N	\N	\N	0	0	0	0	National University of Singapore	Singapore	Yoke Hwee Chan	KK Women's and Children's Hosptial	Singapore	Kerry Chan & Fabian Yap	\N	2024-11-23	\N	850	\N	\N	\N	\N	Co-developed with Caroline Chandler and Minzhi Xing	Asia	f
Frederick	Helyne	helyne@email.unc.edu	Spring 2021	School of Education	Human Development & Family Science	EDUC	475	\N	1	Child and Family Health	\N	\N	\N	\N	\N	\N	25	25	30	29	St. George's University	Grenada	Arlette Herry	\N	\N	\N	\N	2024-10-20	1	2500	1500	\N	\N	\N	\N	North America	f
Ghazi	Noor	nghazi@unc.edu	Fall 2024	College of Arts & Sciences	Peace War and Defense	PWAD	490	()041	1	Conflict in Iraq's Modern History	\N	\N	\N	\N	\N	\N	25	20	\N	\N	Mosul University	Iraq	Ali Albaroodi	\N	\N	\N	\N	2024-08-24	no	2500	\N	\N	\N	\N	\N	Middle East	f
Go	Vivian	vgo@unc.edu	Fall 2022	Gillings School of Global Public Health	Health Behavior	HBEH	784	\N	1	Implementation Science for Global Health	\N	\N	Fall	2022	\N	\N	8	10	10	10	Hanoi Medical University	Vietnam	Le Minh Giang	\N	\N	\N	\N	2024-05-22	1	2500	1500	 Yes 	\N	\N	10 students in COIL component (46 FDOC and 44 LDOC for entire class)	Asia	f
Go	Vivian	vgo@unc.edu	Fall 2021	Gillings School of Global Public Health	Health Behavior	HBEH	784	1	1	Implementation Science in Global Health	\N	\N	\N	\N	\N	\N	12	12	3	3	Hanoi Medical University	Vietnam	Le Minh Giang	\N	\N	\N	\N	2024-03-21	1	2500	1500	\N	\N	\N	Only 3 students participated in COIL component (out of 32)	Asia	f
Gulledge	Suzanne	sgulledg@email.unc.edu	Spring 2021	School of Education	Education	EDUC	526	1	1	Ethics and Education	\N	\N	\N	\N	\N	\N	27	13	23	23	University of Hamburg	Germany	Andreas Bonnet 	\N	\N	\N	\N	2024-06-20	no	3000	\N	\N	\N	\N	\N	Europe	f
Havice	Elizabeth	havice@email.unc.edu	Fall 2020	College of Arts & Sciences	Geography	GEOG	803	\N	1	Seminar in Nature-Society 	\N	\N	\N	\N	\N	\N	10	10	12	11	King's College London	England	Majed Akhter	\N	\N	\N	\N	2024-06-20	2	3000	1500	\N	\N	\N	Split with 2 grad students	Europe	f
Heitsch	Dorothea	dheitsch@unc.edu	Fall 2024	College of Arts & Sciences	Romance Studies	FREN	150	\N	1	Globalization and the French-Speaking World	\N	\N	Fall	2024	\N	\N	40	100	\N	\N	Université Paul Valéry Montpellier 3	France	Nathalie\tAuger	\N	\N	\N	\N	2024-05-24	1	2500	1500	 Yes 	\N	\N	\N	Europe	f
Heitsch	Dorothea	dheitsch@unc.edu	Fall 2023	College of Arts & Sciences	Romance Studies	FREN	150	\N	1	Globalization and the French-Speaking World	\N	\N	Fall	2023	\N	\N	40	150	\N	40	Université Paul Valéry Montpellier 3	France	Nathalie\tAuger	\N	\N	\N	\N	2024-05-23	1	2500	1500	 Yes 	\N	\N	\N	Europe	f
Heitsch	Dorothea	dheitsch@unc.edu	Fall 2022	College of Arts & Sciences	Romance Studies	FREN	150	\N	1	Globalization and the French-Speaking World	\N	\N	\N	\N	\N	\N	35	30	39	38	Université Paul Valéry Montpellier 3	France	Nicolas Gachon	\N	\N	\N	\N	2024-10-21	1	2500	1500	\N	\N	\N	\N	Europe	f
Johnson	Martin	mlj@email.unc.edu	Fall 2023	College of Arts & Sciences	English & Comparative Literature	ENGL	494	1	1	Research Methods in Film Studies	\N	\N	Fall	2023	\N	\N	20	40	\N	21	King's College London	England	Iain Robert Smith	\N	\N	\N	\N	2024-06-23	1	2500	1500	 Yes 	\N	\N	\N	Europe	f
Johnson	Martin	mlj@email.unc.edu	Spring 2022	College of Arts & Sciences	English & Comparative Literature	ENGL	494	1	1	Research Methods in Film Studies	\N	\N	\N	\N	\N	\N	20	40	17	17	King's College London	England	Iain Robert Smith	\N	\N	\N	\N	2024-03-21	1	2500	1500	\N	\N	\N	\N	Europe	f
Keme	Emil'	edelvall@email.unc.edu	Spring 2021	College of Arts & Sciences	Romance Studies	SPAN	344	1	1	Race and Ethnicity in Latin America	\N	\N	\N	\N	\N	\N	25	25	22	20	Universidad San Francisco de Quito	Ecuador	Michael Hill	\N	\N	\N	\N	2024-10-20	1	2500	1500	\N	\N	\N	\N	Latin America	f
Kittner	Noah	kittner@unc.edu	Fall 2024	Gillings School of Public Health	Department of Environmental Sciences and Engineering	ENVR	548	\N	1	Sustainable Energy Systems	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Nagoya University	Japan	Miho Iryo-Asano	\N	\N	\N	\N	2024-05-24	\N	\N	\N	\N	\N	\N	\N	Asia	f
Knorr	Heather	knorrh@email.unc.edu	Fall 2024	College of Arts & Sciences	Romance Studies	SPAN	329	\N	1	Spanish for Profession and Community Engagement	\N	\N	\N	\N	\N	\N	24	24	\N	\N	Universidad Autónoma de Yucatán	Mexico	Manuel J Herrera Góngora	\N	\N	\N	\N	2024-05-24	2	2500	1500	\N	\N	\N	Split grad award with 2 grad students	Latin America	f
Kris	Michael	mkris@email.unc.edu	Fall 2020	College of Arts & Sciences	Music	MUSC	214	3	1	Brass Chamber Music	\N	\N	\N	\N	\N	\N	12	13	9	9	King's College London	England	Joseph Fort	\N	\N	\N	\N	2024-06-20	no	3000	\N	\N	\N	\N	\N	Europe	f
Kris	Michael	mkris@email.unc.edu	Fall 2021	College of Arts & Sciences	Music	MUSC	105	4 5 and 6	3	Individual Brass Lessons (Sections 4 5 6)	\N	\N	\N	\N	\N	\N	14	9	14	15	Universität Mozarteum	Austria	Norbert Salvenmoser	\N	\N	\N	\N	2024-06-21	no	2500	\N	\N	\N	\N	\N	Europe	f
Lanning	Rhonda	rlanning@unc.edu	Fall 2024	School of Nursing	Nursing	NURS	482	1	1	Reproductive Health and the Nursing Care of the Childbearing Family	\N	\N	Fall	2024	\N	\N	114	100	\N	\N	Western Norway University of Applied Sciences	Norway	Elisabeth Hemnes Aanensen	\N	\N	\N	\N	2024-05-24	1	1250	1500	\N	\N	\N	Co-taught with Cathy Crawford	Europe	f
Lanning	Rhonda	rlanning@unc.edu	Fall 2023	School of Nursing	Nursing	NURS	482	\N	1	Reproductive Health and the Nursing Care of the Childbearing Family	\N	\N	\N	\N	\N	\N	115	50	\N	96	Western Norway University of Applied Sciences	Norway	Elisabeth Hemnes Aanensen	\N	\N	\N	\N	2024-05-23	1	1250	1500	\N	\N	\N	Co-taught with Cathy Crawford	Europe	f
Lanning	Rhonda	rlanning@unc.edu	Spring 2024	School of Nursing	Nursing	NURS	482	\N	1	Reproductive Health and the Nursing Care of the Childbearing Family	\N	\N	Spring	2024	\N	\N	115	50	109	109	Western Norway University of Applied Sciences	Norway	Elisabeth Hemnes Aanensen	\N	\N	\N	\N	2024-01-24	1	1250	1500	 Yes 	 Same course same partner 	\N	Co-taught with Cathy Crawford	Europe	f
Lim	Chih-Ing	chih-ing.lim@unc.edu 	Fall 2022	School of Education	Education	EDMX	716	\N	\N	Early Childhood Assessment and Differentiation	Fall	2022	\N	\N	\N	\N	0	0	0	0	National Institute of Education at the Nanyang Technological University (NIE-NTU)	Singapore	Huichao Xie	\N	\N	\N	\N	2024-04-22	\N	1250	\N	\N	\N	\N	co-taught with Jessica Amsbary	Asia	f
Lim	Chih-Ing	chih-ing.lim@unc.edu	Spring 2025	School of Education	Education	EDMX	710	\N	\N	Early Childhood Leadership	Spring	2025	\N	\N	\N	\N	0	0	0	0	University College Dublin	Ireland	Huichao Xie	\N	\N	\N	\N	2024-05-24	\N	1250	\N	\N	\N	\N	co-taught with Jessica Amsbary	Europe	f
Linden	Tom	linden@unc.edu	Fall 2021	Hussman School of Journalism and Media	Journalism	MEJO	560	1	1	Environmental and Science Journalism	\N	\N	\N	\N	\N	\N	20	20	18	18	University of Navarra	Spain	Bienvenido Leon	\N	\N	\N	\N	2024-10-20	1	2500	1500	\N	\N	\N	\N	Europe	f
Lothspeich	Pamela	ploth@email.unc.edu	Fall 2021	College of Arts & Sciences	Middle Eastern and Asian Studies	ASIA	721	1	1	Transnational Feminisms of the Middle East and South Asia	\N	\N	\N	\N	\N	\N	12	7	4	5	Indian Institute of Technology Patna	India	Priyanka Tripathi	\N	\N	\N	\N	2024-03-21	no	2500	\N	\N	\N	\N	\N	Asia	f
Majewska	Agnieszka	agnmaj@unc.edu	Spring 2024	College of Arts & Sciences	Germanic and Slavic Languages and Literatures	PLSH	402	\N	1	Elementary Polish II	\N	\N	\N	\N	\N	\N	0	10	0	7	University of Wrocław	Poland	Marek Kuźniak	\N	\N	\N	\N	2024-04-24	no	2500	\N	\N	\N	\N	Started later in the semester	Europe	f
Majewska	Agnieszka	agnmaj@unc.edu	Spring 2024	College of Arts & Sciences	Germanic and Slavic Languages and Literatures	PLSH	404	\N	1	Intermediate Polish I	\N	\N	\N	\N	Spring 2024	\N	0	0	0	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	The 4 students listed here are to count for students outside of the course	\N	f
Marquis	Moira	mbradfor@live.unc.edu	Spring 2021	College of Arts & Sciences	English & Comparative Literature	ENGL	266	\N	1	Ecocriticism	\N	\N	\N	\N	\N	\N	25	25	32	32	Friedrich-Alexander-Universität Erlangen-Nürnberg	Germany	Sarah Marak	\N	\N	\N	\N	2024-10-20	requested	2500	\N	\N	\N	\N	didn't find grad student	Europe	f
Meredith	Michael	michael_meredith@kenan-flagler.unc.edu	Spring 2023	Kenan-Flagler Business School	Business	BUSI	201	\N	1	Business in Central Europe: Consulting Skills and International Teaming	\N	\N	Spring	2023	\N	\N	20	20	26	24	Corvinus University	Hungary	Miklos Kozma	\N	\N	\N	\N	2024-11-22	1	2500	1500	 Yes 	\N	\N	\N	Europe	f
Meredith	Michael	michael_meredith@kenan-flagler.unc.edu	Spring 2024	Kenan-Flagler Business School	Business	BUSI	301	\N	1	Business in Central Europe: Consulting Skills and International Teaming	\N	\N	Spring	2024	\N	\N	20	20	16	16	Corvinus University	Hungary	Miklos Kozma	\N	\N	\N	\N	2024-05-23	1	2500	1500	 Yes 	\N	\N	Course previously offered as BUSI 201	Europe	f
Meredith	Michael	Michael_Meredith@kenan-flagler.unc.edu	Spring 2022	Kenan-Flagler Business School	Business	BUSI	201	01S	1	Business in Central Europe	\N	\N	\N	\N	\N	\N	20	20	18	18	Corvinus University	Hungary	Miklos Kozma	\N	\N	\N	\N	2024-03-21	1	2500	1500	\N	\N	\N	\N	Europe	f
Mwazandi	Mohamed	mymzandi@email.unc.edu	Fall 2023	College of Arts & Sciences	 African African American and Diaspora Studies	SWAH	403	\N	1	Intermediate Kiswahili III	\N	\N	\N	\N	\N	\N	10	30	\N	7	Pwani University	Kenya	Nancy Ngowa	\N	\N	\N	\N	2024-06-23	1	2500	1500	 Yes 	\N	\N	\N	Africa	f
Mwazandi	Mohamed	mymzandi@email.unc.edu	Spring 2023	College of Arts & Sciences	 African African American and Diaspora Studies	SWAH	402	\N	1	Elementary Kiswahili II	\N	\N	\N	\N	\N	\N	15	20	7	7	Pwani University	Kenya	Nancy Ngowa	\N	\N	\N	\N	2024-11-22	1	2500	1500	\N	\N	\N	\N	Africa	f
Mwazandi	Mohamed	mymzandi@email.unc.edu	Spring 2024	College of Arts & Sciences	 African African American and Diaspora Studies	SWAH	402	\N	1	Elementary Kiswahili II	\N	\N	Spring	2024	\N	\N	15	15	8	8	Pwani University	Kenya	Nancy Ngowa	\N	\N	\N	\N	2024-11-23	1	2500	1500	\N	\N	\N	\N	Africa	f
Mwazandi	Mohamed	mymzandi@email.unc.edu	Fall 2024	College of Arts & Sciences	 African African American and Diaspora Studies	SWAH	403	\N	1	Intermediate Kiswahili III	\N	\N	Fall	2024	\N	\N	15	15	\N	\N	Pwani University	Kenya	Nancy Ngowa	\N	\N	\N	\N	2024-05-24	1	2500	1500	 Yes 	\N	 Fall 2024 	COIL Champion	Africa	f
P. Davis	Suja	davissp@email.unc.edu	Fall 2024	School of Nursing	Nursing	NURS	691	\N	1	Honors in Nursing Part I	\N	\N	Fall	2024	\N	\N	25	30	\N	\N	Universidad de Monterrey	Mexico	Juan Antonio Valdivia Vazquez	\N	\N	\N	\N	2024-05-24	1	2500	1500	 Yes 	\N	\N	\N	Latin America	f
P. Davis	Suja	davissp@email.unc.edu	Fall 2023	School of Nursing	Nursing	NURS	691	\N	1	Honors in Nursing Part I	\N	\N	\N	\N	\N	\N	15	20	\N	39	Universidad de Monterrey	Mexico	Juan Antonio Valdivia Vázquez	\N	\N	\N	\N	2024-07-23	1	2500	1500	\N	\N	\N	\N	Latin America	f
Papoi	Kristin	papoi@email.unc.edu	Fall 2021	School of Education	Education	EDUC	615	1	1	Schools & Community Collaboration	\N	\N	Fall	2021	\N	\N	30	15	27	29	Universidad San Francisco de Quito	Ecuador	Nascira Ramia	\N	\N	\N	\N	2024-05-21	1	2500	1500	 Yes 	\N	\N	\N	Latin America	f
Papoi	Kristin	papoi@email.unc.edu	Fall 2022	School of Education	Education	EDUC	615	\N	1	School and Community Collaboration	\N	\N	Fall	2022	\N	\N	30	15	29	29	Universidad San Francisco de Quito	Ecuador	Nascira Ramia	\N	\N	\N	\N	2024-08-22	2	2500	1500	 Yes 	\N	\N	Split with 2 grad students	Latin America	f
Papoi	Kristin	papoi@email.unc.edu	Spring 2022	School of Education	Education	EDUC	615	1	1	Schools & Community Collaboration	\N	\N	Spring	2022	\N	\N	30	12	31	31	Universidad San Francisco de Quito	Ecuador	Nascira Ramia	\N	\N	\N	\N	2024-12-21	1	2500	1500	 Yes 	\N	\N	\N	Latin America	f
Papoi	Kristin	papoi@email.unc.edu	Spring 2021	School of Education	Education	EDUC	615	\N	1	Schools & Community Collaboration	\N	\N	\N	\N	\N	\N	15	15	30	30	Universidad San Francisco de Quito	Ecuador	Nascira Ramia	\N	\N	\N	\N	2024-06-20	1	3000	1500	\N	\N	\N	\N	Latin America	f
Parker	April	aparker2@unc.edu	Fall 2024	School of Social Work	\N	SOWO	769	2	1	Cultural Sensitivity: Ways of knowing Being Healing and Honoring Youth and Their Families	\N	\N	\N	\N	\N	\N	20	20	\N	\N	The South African College of Applied Psychology	South Africa	Poppy Masinga	\N	\N	\N	\N	2024-05-24	1	2500	1500	\N	\N	\N	\N	Africa	f
Penton	Rachel	pentonre@email.unc.edu	Fall 2021	College of Arts & Sciences	Psychology	NSCI	320	1	1	Neuropsychopharmacology	\N	\N	\N	\N	\N	\N	35	80	34	35	Monash University	Australia	Andrew Giles	\N	\N	\N	\N	2024-03-21	no	2500	\N	\N	\N	\N	\N	Oceania	f
Pier	David	dpier@email.unc.edu	Fall 2022	College of Arts & Sciences	 African African American and Diaspora Studies	AAAD	320	\N	1	Music of Africa	\N	\N	\N	\N	\N	\N	45	20	40	39	Kyambogo University	Uganda	James Isabirye	\N	\N	\N	\N	2024-10-21	no	2500	\N	\N	\N	\N	\N	Africa	f
Rankin	Audra	alnoble@email.unc.edu	Fall 2024	School of Nursing	Nursing	NURS	746	2	1	Health Care Policy and Leadership	\N	\N	Fall	2024	\N	\N	40	40	\N	\N	Mahidol University	Thailand	Atsadaporn Niyomyart	\N	\N	\N	\N	2024-05-24	\N	2500	\N	Yes	\N	\N	\N	Asia	f
Rankin	Audra	alnoble@email.unc.edu	Fall 2023	School of Nursing	Nursing	NURS	746	2	1	Health Care Policy and Leadership	\N	\N	Fall	2023	\N	\N	40	40	\N	18	Mahidol University	Thailand	Nantanit Van Gulik	\N	\N	\N	\N	2024-06-23	no	2500	\N	Yes	\N	\N	\N	Asia	f
Rankin	Audra	alnoble@email.unc.edu	Fall 2022	School of Nursing	Nursing	NURS	746	2	1	Health Care Policy and Leadership	\N	\N	\N	\N	\N	\N	40	40	32	32	Mahidol University	Thailand	Nantanit Van Gulik	\N	\N	\N	\N	2024-10-21	requested	2500	\N	\N	\N	\N	\N	Asia	f
Raphael-Grimm	Theresa	raphaelg@email.unc.edu 	Fall 2024	School of Nursing	Nursing	NURS	746	1	1	Health Care Policy and Leadership	\N	\N	Fall	2024	\N	\N	35	80	\N	\N	Jonkoping University	Sweden	Maria Bjork	\N	\N	\N	\N	2024-05-24	\N	2500	\N	Yes	\N	\N	\N	Europe	f
Raphael-Grimm	Theresa	trg@unc.edu	Fall 2023	School of Nursing	Nursing	NURS	301	1	1	Foundations of RelationshipCentered Care and Diversity and Inclusion	\N	\N	\N	\N	\N	\N	115	60	\N	111	Jonkoping University	Sweden	Maria Bjork	\N	\N	\N	\N	2024-05-23	1	2500	1500	\N	\N	\N	\N	Europe	f
Raphael-Grimm	Theresa	trg@unc.edu	Fall 2022	School of Nursing	Nursing	NURS	864	1	1	Biopsychosocial Care 3: Psychiatric Mental Health Interventions in the Context of Relationships	\N	\N	Fall	2022	\N	\N	20	60	15	11	Jonkoping University	Sweden	Maria Bjork	\N	\N	\N	\N	2024-12-21	1	2500	1500	 Yes 	\N	\N	\N	Europe	f
Raphael-Grimm	Theresa	trg@unc.edu	Fall 2021	School of Nursing	Nursing	NURS	864	1	1	Biopsychosocial Care 3: Psychiatric Mental Health Interventions in the Context of Relationships	\N	\N	\N	\N	\N	\N	22	60	19	19	Jonkoping University	Sweden	Maria Bjork Elzana Odzakovic Karina Huus Johanna Falck	Uppsala University	Sweden	Sarah Hamed Hannah Bradby	\N	2024-03-21	1	2500	1500	\N	\N	\N	\N	Europe	f
Riger	Dana	driger@unc.edu	Spring 2024	School of Education	Human Development & Family Science	EDUC	375	\N	1	Identity & Sexuality	\N	\N	\N	\N	\N	\N	35	30	38	38	National Taiwan Normal University	Taiwan	Hsi-Peng Nieh	\N	\N	\N	\N	2024-11-23	1	2500	1500	\N	\N	\N	\N	Asia	f
Rivard	Courtney	crivard@email.unc.edu	Spring 2022	College of Arts & Sciences	English & Comparative Literature	ENGL	118	1	1	Storytelling and Game Development	\N	\N	\N	\N	\N	\N	25	40	22	22	King's College London	England	Feng Zhu	\N	\N	Connor McKeown	\N	2024-10-21	1	2500	1500	\N	\N	\N	\N	Europe	f
Rivkin-Fish	Michele	mrfish@unc.edu	Fall 2021	College of Arts & Sciences	Anthropology	ANTH	442	1	1	Health and Gender After Socialism	\N	\N	\N	\N	\N	\N	32	15	33	33	Higher School of Economics University	Russia	Sergei Zakharov	\N	\N	\N	\N	2024-03-21	1	2500	1500	\N	\N	\N	\N	CSEEES	f
Rosenmeyer	Patricia	patanne@email.unc.edu	Fall 2021	College of Arts & Sciences	Classics	CLAS	363H	1	1	Greek & Latin Poetry in Translation	\N	\N	\N	\N	\N	\N	20	15	13	11	Universidade de São Paulo	Brazil	Giuliana Ragusa de Faria	\N	\N	\N	\N	2024-10-20	1	2500	1500	\N	\N	\N	\N	Latin America	f
Saba	Markus	markus_saba@kenan-flagler.unc.edu	Fall 2021	Kenan-Flagler Business School	Business	MBA	899	1	1	Healthcare in the Age of COVID	\N	\N	Fall	2021	\N	Q2	20	20	17	17	Strathmore University 	Kenya	Ben Ngoye	\N	\N	\N	\N	2024-05-21	no	2500	\N	 Yes 	\N	\N	\N	Africa	f
Saba	Markus	markus_saba@kenan-flagler.unc.edu	Fall 2022	Kenan-Flagler Business School	Business	MBA	899	3	1	Healthcare in the Age of COVID	\N	\N	Fall	2022	\N	Q2	25	20	24	24	Strathmore University 	Kenya	Ben Ngoye	\N	\N	\N	\N	2024-08-22	no	2500	0	Yes	\N	\N	\N	Africa	f
Saba	Markus	markus_saba@kenan-flagler.unc.edu	Fall 2020	Kenan-Flagler Business School	Business	MBA	899	\N	1	Healthcare in the Age of COVID	\N	\N	\N	\N	\N	Q2	20	15	13	12	Strathmore University 	Kenya	Ben Ngoye	\N	\N	\N	\N	2024-06-20	1	3000	1500	\N	\N	\N	\N	Africa	f
Saba	Markus	markus_saba@kenan-flagler.unc.edu	Fall 2024	Kenan-Flagler Business School	Business	MBA	899	1	1	Innovation in Healthcare: Comparative Health Systems in Romania and the U.S.	\N	\N	\N	\N	\N	\N	25	25	\N	\N	Babes-Bolyai University	Romania	Levente Szasz	\N	\N	\N	\N	2024-05-24	no	2500	0	\N	\N	\N	Same course number different partner	\N	f
Sawin	Patricia	sawin@unc.edu	Spring 2021	College of Arts & Sciences	American Studies	FOLK/ENGL	487	\N	1	Everyday Stories 	\N	\N	\N	\N	\N	\N	26	50	25	21	University College Dublin	Ireland	Tiber Falzett	\N	\N	\N	\N	2024-06-20	1	\N	1500	\N	\N	\N	didn't want award just for grad	Europe	f
Sibley	Caroline	caroline.sibley@unc.edu	Spring 2025	College of Arts & Sciences	Asian and Middle Eastern Studies	ARAB	102	\N	1	Elementary Arabic II	\N	\N	\N	\N	\N	\N	16	10	\N	\N	Universite Sidi Mohamed Ben Abdellah	Morocco	Othmane Zakaria	\N	\N	\N	\N	2024-05-24	\N	2500	\N	\N	\N	\N	\N	Africa	f
Sibley	Caroline	robinsoc@email.unc.edu 	Spring 2024	College of Arts & Sciences	Middle Eastern and Asian Studies	ARAB	306	\N	1	Advanced Arabic	\N	\N	\N	\N	\N	\N	15	15	12	22	Mohammed VI Polytechnic University	Morocco	Jennifer Crespo	\N	\N	\N	\N	2024-05-23	1	2500	1500	\N	\N	\N	\N	Africa	f
Siegal McIntyre	Erin	esm@unc.edu	Fall 2024	Hussman School of Journalism and Media	Journalism	MEJO	553	1	1	Advanced Reporting	\N	\N	Fall	2024	\N	\N	10	12	\N	\N	Universidad Autónoma de Baja California	Mexico	Viviana Mejía Cañedo	\N	\N	\N	\N	2024-06-24	requested	2500	\N	 Yes 	\N	\N	\N	Latin America	f
Siegal McIntyre	Erin	esm@unc.edu	Spring 2022	Hussman School of Journalism and Media	Journalism	MEJO	553	1	1	Advanced Reporting	\N	\N	\N	\N	\N	\N	18	15	12	12	Universidad Autónoma de Baja California	Mexico	Viviana Mejía Cañedo	\N	\N	\N	\N	2024-10-21	1	2500	1500	\N	\N	\N	\N	Latin America	f
Szypszak	Charles	szypszak@sog.unc.edu	Spring 2023	School of Government	Government	POLI	290	\N	1	Special Topics in Political Science	\N	\N	\N	\N	\N	\N	12	12	10	10	Vilnius University	Lithuania	Donatas Murauskas	\N	\N	\N	\N	2024-07-22	1	2500	1500	\N	\N	\N	\N	CSEEES	f
Taj	Afroz	taj@unc.edu	Spring 2022	College of Arts & Sciences	Middle Eastern and Asian Studies	ASIA	231	1	1	Bollywood Cinema	\N	\N	\N	\N	\N	\N	75	30	59	58	Jamia Millia Islamia	India	Nishat Zaidi	\N	\N	\N	\N	2024-03-21	no	2500	\N	\N	\N	\N	\N	Asia	f
Tasar	Eren	etasar@email.unc.edu	Summer 2024	College of Arts & Sciences	History	HIST	140	\N	1	World Since 1945	\N	\N	\N	\N	\N	\N	25	25	30	29	Humboldt University of Berlin	Germany	Lukas Lammers	\N	\N	\N	\N	2024-05-24	1	2500	1500	\N	\N	\N	\N	Europe	f
Thompson	Amanda	althomps@email.unc.edu	Fall 2020	College of Arts & Sciences	Anthropology	ANTH	190	\N	1	Intro to Biocultural Medical Anthropology	\N	\N	\N	\N	\N	\N	45	45	39	36	Universidad San Francisco de Quito	Ecuador	Diego Quiroga	\N	\N	\N	\N	2024-06-20	1	3000	1500	\N	\N	\N	\N	Latin America	f
Truong	Lien	lien.truong@unc.edu	Fall 2020	College of Arts & Sciences	Art & Art History	ARTS	322	\N	1	Narrative Painting	\N	\N	\N	\N	\N	\N	15	15	9	9	Vietnam University of Fine Arts	Vietnam	Theson Nguyen	\N	\N	\N	\N	2024-06-20	1	3000	1500	\N	\N	\N	\N	Asia	f
Vachudova	Milada	vachudov@email.unc.edu	Fall 2020	College of Arts & Sciences	Political Science	POLI	438	\N	1	Undivided Europe	\N	\N	\N	\N	\N	\N	30	100	22	20	King's College London	England	Hanna Kleider	\N	\N	\N	\N	2024-06-20	1	3000	1500	\N	\N	\N	\N	Europe	f
Valdivia	Gabriela	valdivia@email.unc.edu	Fall 2022	College of Arts & Sciences	Geography	GEOG	457	\N	1	Rural Latin America	\N	\N	\N	\N	\N	\N	24	30	24	24	Universidad del Norte	Colombia	Eloisa Berman Arévalo	\N	\N	\N	\N	2024-10-21	1	2500	1500	\N	\N	\N	\N	Latin America	f
Versenyi	Adam	anversen@email.unc.edu	Spring 2022	College of Arts & Sciences	Dramatic Art	DRAM	284	1	1	Theatre and Pandemic Theatre After Pandemic	\N	\N	Spring	2022	\N	\N	15	15	16	16	Queen's University Belfast 	Northern Ireland	Kurt Taroff	National University of Ireland Galway	Ireland	Patrick Lonergan	\N	2024-05-21	1	2500	1500	 Yes 	\N	\N	\N	Europe	f
Versenyi	Adam	anversen@email.unc.edu	Spring 2023	College of Arts & Sciences	Dramatic Art	DRAM	284	\N	1	Theatre and Democracy	\N	\N	Spring	2023	\N	\N	15	30	15	15	Queen's University Belfast 	Northern Ireland	Kurt Taroff	National University of Ireland Galway	Ireland	Patrick Lonergan	\N	2024-11-22	1	2500	1500	 Yes 	\N	\N	\N	Europe	f
Versenyi	Adam	anversen@email.unc.edu	Spring 2021	College of Arts & Sciences	Dramatic Art	DRAM	284	\N	1	Theatre and Pandemic	\N	\N	\N	\N	\N	\N	15	15	6	6	Queen's University Belfast 	Northern Ireland	Kurt Taroff	National University of Ireland Galway	Ireland	Patrick Lonergan	\N	2024-06-20	1	3000	1500	\N	\N	\N	\N	Europe	f
Villegas	Natalia	navilleg@email.unc.edu	Spring 2021	School of Nursing	Nursing	NURS	320	\N	1	Culture and Nursing Care	\N	\N	\N	\N	\N	\N	60	60	6	6	Pontificia Universidad Católica de Chile	Chile	Marcela Gonzalez	\N	\N	Solange Campos	\N	2024-10-20	no	2500	\N	\N	\N	\N	\N	Latin America	f
Villegas	Natalia	navilleg@email.unc.edu\r	Spring 2024	School of Nursing	Nursing	NURS	320	\N	1	Culture and Nursing Care	\N	\N	\N	\N	\N	\N	30	30	23	23	Universidad Francisco de Vitoria	Spain	Mariana Aline Renghea	\N	\N	\N	\N	2024-12-23	1	2500	1500	\N	\N	\N	\N	Europe	f
Walters	Elizabeth	elizabeth_walters@unc.edu	Spring 2022	School of Nursing	Nursing	NURS	740	\N	\N	Evidence-based Practice and Research	Spring	2022	\N	\N	\N	\N	0	0	0	0	Chiang Mai University	Thailand	Patraporn Tungpunkom	\N	\N	\N	\N	2024-03-21	\N	1250	\N	\N	\N	\N	co-taught with Leslie Davis	Asia	f
Watts-Isley	Jaimee	jwisley@email.unc.edu	Spring 2021	School of Nursing	Nursing	NURS	402C	\N	1	Foundations of Population Health and Global Health	\N	\N	\N	\N	\N	\N	100	100	104	104	Australian Catholic University	Australia	Jacqui Young	\N	\N	\N	\N	2024-10-20	1	1250	1500	\N	\N	\N	co-taught with Meg Zomorodi	Oceania	f
Weed	Kym	kweed@unc.edu	Fall 2024	College of Arts & Sciences	English & Comparative Literature	ENGL	763	\N	1	Intro to Methods in Health Humanities	\N	\N	\N	\N	\N	\N	15	10	\N	\N	Exeter University	England	Michael Flexer	\N	\N	\N	\N	2024-11-23	1	2500	1500	\N	\N	\N	\N	Europe	f
Woodley	Lisa	lwoodley@email.unc.edu	Fall 2024	School of Nursing	Nursing	NURS	483	\N	1	Family-Centered Nursing Care from Birth Through Adolescence	\N	\N	Fall	2024	\N	\N	100	40	\N	\N	Universidade de São Paulo	Brazil	Maiara Rodrigues dos Santos	\N	\N	\N	\N	2024-05-24	1	1000	1500	Yes	\N	Fall 2024	COIL Champion; Co-taught with Beth Cosgrove	Latin America	f
Woodley	Lisa	lwoodley@email.unc.edu	Fall 2022	School of Nursing	Nursing	NURS	483	1	1	Family-Centered Nursing Care from Birth Through Adolescence	\N	\N	Fall	2022	\N	\N	100	40	102	102	Universidade de São Paulo	Brazil	Maiara Rodrigues dos Santos	\N	\N	\N	\N	2024-08-22	1	2500	1500	 Yes 	\N	\N	\N	Latin America	f
Woodley	Lisa	lwoodley@email.unc.edu	Spring 2022	School of Nursing	Nursing	NURS	483	1	1	Family-Centered Nursing Care from Birth Through Adolescence	\N	\N	Spring	2022	\N	\N	100	40	99	99	Universidade de São Paulo	Brazil	Maiara Rodrigues dos Santos	\N	\N	\N	\N	2024-08-21	1	2500	1500	 Yes 	\N	\N	\N	Latin America	f
Woodley	Lisa	lwoodley@email.unc.edu	Fall 2021	School of Nursing	Nursing	NURS	483	\N	1	Family-Centered Nursing Care from Birth Through Adolescence	\N	\N	\N	\N	\N	\N	100	40	102	102	Universidade de São Paulo	Brazil	Maiara Rodrigues dos Santos	\N	\N	\N	\N	2024-03-21	1	2500	1500	\N	\N	\N	\N	Latin America	f
Woodley	Lisa	lwoodley@email.unc.edu	Fall 2023	School of Nursing	Nursing	NURS	483	\N	1	Family-Centered Nursing Care from Birth Through Adolescence	\N	\N	Fall	2023	\N	\N	100	40	\N	113	Universidade de São Paulo	Brazil	Maiara Rodrigues dos Santos	\N	\N	\N	\N	2024-08-23	no	1250	\N	\N	\N	Fall 2023	Co-taught with Beth Cosgrove	Latin America	f
Woodley	Lisa	lwoodley@email.unc.edu	Spring 2024	School of Nursing	Nursing	NURS	483	\N	1	Family-Centered Nursing Care from Birth Through Adolescence	\N	\N	Spring	2024	\N	\N	100	40	96	96	Universidade de São Paulo	Brazil	Maiara Rodrigues dos Santos	\N	\N	\N	\N	2024-11-23	\N	1250	\N	\N	\N	Spring 2024	Co-taught with Beth Cosgrove	Latin America	f
Xing	Minzhi	Minzhi.Xing@unc.edu	Spring 2025	Gillings School of Public Health	Public Health Leadership	MHCH	728	\N	\N	Implementation Research and Practice in Maternal Child and Family Health	Spring	2025	\N	\N	\N	\N	0	0	0	0	National University of Singapore	Singapore	Yoke Hwee Chan	KK Women's and Children's Hosptial	Singapore	Kerry Chan & Fabian Yap	\N	2024-11-23	requested	850	\N	\N	\N	\N	Co-developed with Oscar Flemming and Caroline Chandler	Asia	f
Yaghoobi	Claudia	yaghoobi@email.unc.edu	Fall 2021	College of Arts & Sciences	Middle Eastern and Asian Studies	ASIA/CMPL	127	1	1	Iranian Women Writers	\N	\N	\N	\N	\N	\N	35	30	26	25	University of British Columbia	Canada	Mostafa Abedinifard	\N	\N	\N	\N	2024-03-21	no	2500	\N	\N	\N	\N	\N	North America	f
Yaghoobi	Claudia	yaghoobi@email.unc.edu	Spring 2022	College of Arts & Sciences	Middle Eastern and Asian Studies	ASIA	69	1	1	Wars and Veterans: Iran Iraq and Afghanistan	\N	\N	\N	\N	\N	\N	24	20	11	11	Shiraz University	Iran	Amir Vafa	\N	\N	\N	\N	2024-10-21	no	2500	\N	\N	\N	\N	\N	Mideast	f
Zhou	Yi	yizh@email.unc.edu	Fall 2024	College of Arts & Sciences	Middle Eastern and Asian Studies	CHIN	305	1 and 2	2	Advanced Chinese I	\N	\N	Fall	2024	\N	\N	40	45	\N	\N	Tianjin Normal University	China	Xiuhong (Samantha) Shi	\N	\N	\N	\N	2024-05-24	\N	2500	\N	Yes	\N	\N	\N	Asia	f
Zhou	Yi	yizh@email.unc.edu	Fall 2022	College of Arts & Sciences	Middle Eastern and Asian Studies	CHIN	443	\N	1	Business Communications in Chinese	\N	\N	\N	\N	\N	\N	18	6	21	20	Beijing Normal University	China	Hang Ke	\N	\N	\N	\N	2024-07-22	no	2500	\N	\N	\N	\N	\N	Asia	f
Zhou	Yi	yizh@email.unc.edu	Fall 2023	College of Arts & Sciences	Middle Eastern and Asian Studies	CHIN	305	1 and 2	2	Advanced Chinese I	\N	\N	\N	\N	\N	\N	40	45	\N	32	Tianjin Normal University	China	Xiuhong (Samantha) Shi	\N	\N	\N	\N	2024-11-22	1	2500	1500	\N	\N	\N	\N	Asia	f
Zhou	Yi	yizh@email.unc.edu	Spring 2023	College of Arts & Sciences	Middle Eastern and Asian Studies	CHIN	306	\N	1	Advanced Chinese II	\N	\N	\N	\N	\N	\N	38	45	34	33	Tianjin Normal University	China	Xiuhong (Samantha) Shi	\N	\N	\N	\N	2024-11-22	1	2500	1500	 Yes 	\N	\N	\N	Asia	f
Zomorodi	Meg	meg_zomorodi@unc.edu	Spring 2022	School of Nursing	Nursing	NURS	402	1	1	Foundations of Population Health and Global Health: Carolina Core IV	\N	\N	Spring	2022	\N	\N	100	200	93	93	Australian Catholic University	Australia	Jacqui Young	\N	\N	\N	\N	2024-12-21	1	2500	1500	 Yes 	\N	\N	requested grad student. check.	\N	f
Zomorodi	Meg	meg_zomorodi@unc.edu	Spring 2021	School of Nursing	Nursing	NURS	402C	\N	\N	Foundations of Population Health and Global Health	Spring	2021	\N	\N	\N	\N	0	0	0	0	Australian Catholic University	Australia	Jacqui Young	\N	\N	\N	\N	2024-10-20	\N	1250	\N	\N	\N	\N	Co-taught with Jaimee Watts-Isley	\N	f
Lepofsky	Jonathan	lepofsky@email.unc.edu	find out	College of Arts & Sciences	Geography	GEOG	468-001(?)	\N	\N	Environmental Justice in Urban Europe	CANCELLED	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2024-03-21	no	2500	\N	\N	\N	\N	would have been with university in Comenius in Slovakia Paid May 2021.	\N	t
Van Riper	Marcia	vanriper@email.unc.edu	find out	School of Nursing	Nursing	NURS	960-001	\N	\N	Individual and Family Responses to Chronic Conditions	CANCELLED	\N	\N	\N	\N	\N	15	15	\N	\N	\N	\N	\N	\N	\N	\N	\N	2024-10-21	requested	2500	\N	\N	\N	\N	would have been with Maiara dos Santos with USP. Paid Feb. 2022.	\N	t
Layne	Priscilla	playne@email.unc.edu	find out	College of Arts & Sciences	Germanic & Slavic Language & Literature	GERM	278	\N	\N	Performance Drama Translation Adaptation and Ethnographic Exchange	CANCELLED	\N	\N	\N	\N	\N	10	22	\N	\N	\N	\N	Joseph Megel and Henning Bochert	\N	\N	\N	\N	2024-12-21	yes 	\N	\N	\N	\N	\N	class canceled	\N	t
Siegal McIntyre	Erin	esm@unc.edu	Fall 2023	Hussman School of Journalism and Media	\N	MEJO	553	\N	\N	Advanced Reporting	DELAYED	\N	Fall	2023	\N	\N	20	20	\N	\N	Universidad Autónoma de Baja California	Mexico	Viviana Mejia Canedo	\N	\N	\N	\N	\N	requested	\N	\N	\N	\N	\N	Delayed because has fellowship	\N	t
Villegas	Natalia	navilleg@email.unc.edu	Spring 2024	School of Nursing	Nursing	NURS	320	\N	\N	Culture and Nursing Care	DELAYED	\N	Spring	2024	\N	\N	40	80	\N	\N	Pontificia Universidad Católica de Chile	Chile	Marcela Gonzalez	\N	\N	Solange Campos	\N	2024-12-22	requested	\N	\N	\N	\N	\N	Delayed	\N	t
Szypszak	Charles	szypszak@sog.unc.edu	Spring 2024	School of Government	\N	POLI	290	\N	\N	Special Topics in Political Science	Low enrollment for course - CANCELED	\N	Spring	2024	\N	\N	12	12	\N	\N	Vilnius University	Lithuania	Donatas Murauskas	\N	\N	\N	\N	2024-05-23	requested	\N	\N	\N	\N	\N	\N	\N	t
Baker	Maureen	mjbaker@ad.unc.edu	Fall 2024	School of Nursing	Nursing	NURS	934-001	\N	\N	Clinical Scholarship and Professional Communication	Cancelled COIL component	\N	Fall	2024	\N	\N	18	14	\N	\N	St. Luke's International University	Japan	Erika Ota	\N	\N	\N	\N	2024-11-23	1	1500	1500	\N	\N	\N	 Skipping this semester and hopes to pickup again 	\N	t
Davis	Leslie	lldavis@email.unc.edu	find out	\N	\N	\N	\N	\N	\N	find out	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2024-12-22	1	1250	1500	\N	\N	\N	\N	\N	t
Palmer	Carrie	cfarr@email.unc.edu	find out	School of Nursing	Nursing	\N	\N	\N	\N	find out	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2024-01-23	\N	1250	\N	\N	\N	\N	\N	\N	t
\.


--
-- Data for Name: grad_student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.grad_student ("Semester Taught", "Year Taught", "Last Name", "First Name", "Faculty Supervisor", "School", "Department", "Course", "Number", "UNC Course Name", "Partner Institution", "Award", "TA Email", "TA PID") FROM stdin;
Summer	2024	Shtumpf	Alexandr	Eren Tasar	College of Arts & Sciences	History	HIST	140	World Since 1945	Humboldt University of Berlin	750	\N	\N
Spring	2022	Goldych	Alexandra	Martin Johnson	College of Arts & Sciences	English & Comparative Literature	ENGL	494	Research Methods in Film Studies	King's College London	750	\N	730341411
Fall	2022	Goldych	Alexandra (Alex)	Dorothea Heitsch	College of Arts & Sciences	Romance Studies	FREN	150	Globalization and the French Speaking World	Université Paul Valéry Montpellier 3	1500	\N	\N
Spring	2023	Young	Alinda	Mohamed Mwamzandi	Gillings School of Global Public Health	\N	SWAH	402	Elementary Kiswahili II	Pwani University	1500	\N	\N
Fall	2023	Young	Alinda	Mohamed Mwamzandi	Gillings School of Global Public Health	Health Behavior	SWAH	403	Intermediate Kiswahili I	Pwani University	1500	\N	\N
Spring	2024	Young	Alinda	Mohamed Mwamzandi	Gillings School of Global Public Health	\N	SWAH	402	Elementary Kiswahili II	Pwani University	1500	\N	\N
Fall	2020	Suk	Ann	Amanda Thompson	College of Arts & Sciences	Anthropology	ANTH	190	Intro to Biocultural Medical Anthropology	Universidad San Francisco de Quito	1500	\N	\N
Fall	2021	Hugosson	Annika 	Michele Rivkin-Fish	College of Arts & Sciences	Anthropology	ANTH	442	Health and Gender After Socialism	Higher School of Economics	1500	hugosson@email.unc.edu	\N
Fall	2024	Bamogo	Assanatou	Mohamed Mwamzandi	College of Arts & Sciences	African, African American & Diaspora Studies	SWAH	403	Intermediate Kiswahili III	Pwani University	1500	\N	\N
Spring	2021	Sostaita	Barbara	Emil' Keme	College of Arts & Sciences 	Romance Studies	SPAN	344	Race and Ethnicity in Latin America	Universidad San Francisco de Quito	1500	bsostaita@unc.edu	\N
Fall	2024	Meinke	Bart	Dorothea Heitsch	College of Arts & Sciences	Romance Studies	FREN	150	Globalization and the French Speaking World	Université Paul Valéry Montpellier 3	1500	\N	\N
Spring	2023	Downs	Bradley	Charles Szypszak	School of Government	\N	POLI	290	Special Topics in Political Science	Vilnius University	1500	\N	\N
Fall	2024	López Parí 	Carlos Rubens	Heather Knorr	College of Arts & Sciences	Romance Studies	SPAN	329	Spanish for Profession and Community Engagement	Universidad  Autónoma de Yucatán	1500	\N	\N
Fall	2024	Larios	Celina	Heather Knorr	College of Arts & Sciences	Romance Studies	SPAN	329	Spanish for Profession and Community Engagement	Universidad  Autónoma de Yucatán	1500	\N	\N
Fall	2020	Ziobro	Dale	Markus Saba	Kenan-Flagler Business School	Business	MBA	899	Healthcare in the Age of COVID	Strathmore University	1500	\N	\N
Spring	2021	Dilliplane	Dan	Adam Versenyi	College of Arts & Sciences 	Dramatic Art	DRAM	284	Theatre and Pandemic	Queen's University Belfast / National University of Ireland, Galway	750	dandill@live.unc.edu	\N
Spring	2022	Dilliplane	Dan	Adam Versenyi	College of Arts & Sciences	Dramatic Art	DRAM	284	Theatre & Pandemic, Theatre After Pandemic	Queen's University Belfast/Northern Ireland	750	\N	730105548
Spring	2022	Earixson	Dan	Kristin Papoi	School of Education	 	EDUC	615	Schools and Community Collaboration	Universidad San Francisco de Quito	1500	\N	730028070
Spring	2021	Earixson	Daniel	Kristin Papoi	School of Education 	Education	EDUC	615	Schools & Community Collaboration	Universidad San Francisco de Quito	1500	dan_earixson@med.unc.edu	\N
Fall	2021	Earixson	Daniel	Kristin Papoi	School of Education 	Education	EDUC	615	Schools & Community Collaboration	Universidad San Francisco de Quito	1500	dan_earixson@med.unc.edu	\N
Fall	2023	Baker Gill	David	Dorothea Heitsch	College of Arts & Sciences	Romance Studies	FREN	150	Globalization and the French Speaking World	Université Paul Valéry Montpellier 3	1500	\N	\N
Fall	2020	Corin	Deanna 	Elizabeth Havice	College of Arts & Sciences 	Geography	GEOG	803	Seminar in Nature-Society 	King's College London	1500	\N	\N
Fall	2021	Kamkhoad	Donruedee	Maureen Baker	School of Nursing	\N	NURS	934	Clinical Scholarship and Professional Communication	St. Luke's International University	1500	yuidk@live.unc.edu	\N
Fall	2022	Kamkhoad	Donruedee	Maureen Baker	School of Nursing	\N	NURS	934	Clinical Scholarship and Professional Communication	St. Luke’s International University	1500	\N	\N
Fall	2022	Dedushaj	Dorentina	Jessica Amsbary	School of Education	\N	EDUC	716	Assessment and Differentiation	National Institute of Education at the Nanyang Technological University	1500	\N	\N
Spring	2022	Stark	Doug	Courtney Rivard	College of Arts & Sciences	English & Comparative Literature	ENGL	118	Storytelling and Game Development	King's College London	1500	\N	730184751
Fall	2022	Delvalle	Elena	Kristin Papoi	School of Education	\N	EDUC	615	Schools & Community Collaboration	Universidad San Francisco de Quito	1500	\N	\N
Fall	2022	Banks	Emily	Kristin Papoi	School of Education	\N	EDUC	615	Schools & Community Collaboration	Universidad San Francisco de Quito	1500	\N	\N
Spring	2023	Ashammari	Fadhah	Leslie Davis	School of Nursing	\N	NURS	740	Evidence-based Practice and Research	King Saud University	1500	\N	\N
Spring	2023	Ishak	Farisha	Michael Meredith	Kenan-Flagler Business School	\N	BUSI	201	Business in Europe	Corvinus University	1500	\N	\N
Spring	2024	Ishak	Farisha	Michael Meredith	Kenan-Flagler Business School	\N	BUSI	201	Business in Europe	Corvinus University	1500	\N	\N
Fall	2021	Grant	Gabrielle	Lisa Woodley	School of Nursing	\N	NURS	483	Family-Centered Nursing Care from Birth Through Adolescence	University of Sao Paulo	1500	gabgrant@email.unc.edu	\N
Spring	2022	Grant 	Gabrielle	Lisa Woodley	School of Nursing	 	NURS	483	Family-Centered Nursing Care from Birth Through Adolescence	University of Sao Paulo	1500	\N	730385675
Fall	2022	Grant	Gabrielle	Lisa Woodley	School of Nursing	\N	NURS	483	Family-Centered Nursing Care from Birth Through Adolescence	University of Sao Paulo	1500	\N	\N
Spring	2023	Grant	Gabrielle	Beth Cosgrove	School of Nursing	\N	NURS	483	Family-Centered Nursing Care from Birth Through Adolescence	University of Sao Paulo	1500	\N	\N
Fall	2023	Grant	Gabrielle	Beth Cosgrove	School of Nursing	\N	NURS	483	Family-Centered Nursing Care from Birth Through Adolescence	Universidade de Sao Paulo	1500	\N	\N
Fall	2023	Grant	Gabrielle	Rhonda Lanning and Catherine Crawford	School of Nursing	\N	NURS	482	Reproductive Health and Nursing Care of the Childbearing Family	Western Norway University of Applied Sciences	1500	\N	\N
Spring	2024	Grant	Gabrielle	Beth Cosgrove	School of Nursing	\N	NURS	483	Family-Centered Nursing Care from Birth Through Adolescence	Universidade de Sao Paulo	750	\N	\N
Spring	2024	Grant	Gabrielle	Rhonda Lanning and Catherine Crawford	School of Nursing	\N	NURS	482	Reproductive Health and Nursing Care of the Childbearing Family	Western Norway University of Applied Sciences	750	\N	\N
Fall	2021	Huffstetler	Hanna	Vivian Go	Gillings School of Global Public Health	\N	HBEH	784	Implementation Science in Global Health	Hanoi Medical University	1500	hhuffste@live.unc.edu	\N
Fall	2022	Diaz-Moreno	Ingrid	Gabriela Valdivia	College of Arts & Sciences	Geography	GEOG	457	Rural Latin America	Universidad del Norte	1500	\N	\N
Spring	2024	Ramirez	Janette	Lisa Domby	School of Medicine	\N	SPHS	751	Global Issues & Practices in Communication Sciences & Disorders	Universidad Rafael Landivar	1500	\N	\N
Spring	2022	Nance	Jennifer	Leslie Davis & Elizabeth Walters	School of Nursing	 	NURS	740	Evidence-based Practice and Research	Chiang Mai University	1500	\N	720391344
Spring	2023	O'Connell	Joseph	Gabrielle Berlinger	College of Arts & Sciences	American Studies	FOLK/ANTH	424	Ritual/Festival/Public Culture	University College Dublin	750	\N	\N
Fall	2021	Villa-Palomino	Julio	Florence Babb	College of Arts & Sciences	Anthropology	LTAM	101	Introduction to Latin American Studies	University of Navarra	750	juliovp@live.unc.edu	\N
Fall	2022	Villa-Palomino	Julio	Florence Babb	College of Arts & Sciences	Anthropology	LTAM	101	Intro to Latin American Studies	Universidad San Francisco de Quito	1500	\N	\N
Fall	2023	Gutierrez	Julio	Florence Babb	College of Arts & Sciences	Anthropology	LTAM	101	Introduction to Latin American Studies	Universidad San Francisco de Quito	1500	\N	\N
Spring	2024	Maganga	Laika	Natalia Villegas Rodriguez	School of Nursing	\N	NURS	320	Culture and Nursing Care	Universidad Francisco de Vitoria	1500	\N	\N
Fall	2021	Jeranko	Maja	Florence Babb	College of Arts & Sciences	Anthropology	LTAM	101	Introduction to Latin American Studies	Universidade de São Paulo	1500	mjeranko@live.unc.edu	\N
Fall	2022	Jeranko	Maja	Florence Babb	College of Arts & Sciences	Anthropology	LTAM	101	Intro to Latin American Studies	Universidad San Francisco de Quito	1500	\N	\N
Spring	2022	Jaramillo	Maria Elizabeth	Lisa Domby	School of Medicine	Allied Health Sciences	SPHS	751	Global Issues & Practices in Communication Sciences & Disorders	Universidad Rafael Landivar	1500	\N	730267376
Spring	2023	Jaramillo	Maria Elizabeth	Lisa Domby	School of Medicine	Allied Health Sciences	SPHS	751	Global Issues & Practices in Communication Sciences & Disorders	Universidad Rafael Landivar	1500	\N	\N
Fall	2020	Naunov	Martin	Milada Vachudova	College of Arts & Sciences 	Political Science	POLI	438	Undivided Europe	King's College London	1500	\N	\N
Spring	2022	Killela	Mary	Meg Zomorodi	School of Nursing	 	NURS	402	Foundations of Population Health and Global Health: Carolina Core IV	Australian Catholic University	1500	\N	720143081
Fall	2020	Biggs	Mary 	Elizabeth Havice	College of Arts & Sciences	Geography	GEOG	803	Seminar in Nature-Society 	King's College London	1500	\N	\N
Spring	2021	Killela	Mary \t\t	Meg Zomorodi	School of Nursing	Nursing	NUR	402C	Foundations of Population Health and Global Health	Australian Catholic University	1500	mkillela@email.unc.edu	\N
Spring	2022	Mannen	Mary Leighton	Michael Meredith	Kenan-Flagler Business School	 	BUSI	201	Business in Central Europe	Corvinus University	1500	\N	730082226
Spring	2023	Foster	Megan	Adam Versenyi	College of Arts & Sciences	Communication	DRAM	284	Theatre and Democracy	National University of Ireland, Galway and Queen's University, Belfast	1500	\N	\N
Fall	2024	Jesudoss	Mercy	Suja Davis	School of Nursing	\N	NURS	691	Honors Seminar Part 1	Universidad de Monterrey	1500	\N	\N
Spring	2023	Baird	Michael Shane	Raphael Birya	College of Arts & Sciences	Art History	SWAH	402	Elementary Kiswahili II	Pwani University	1500	\N	\N
Fall	2023	Baird	Michael Shane	Raphael Birya	College of Arts & Sciences	History	SWAH	403	Kiswahili Intermediate I	Pwani University	1500	\N	\N
Fall	2024	Madison	Miriam	April Parker	School of Social Work	\N	SOWO	769	Cultural Sensitivity: Ways of Knowing, Being, Healing, and Honoring Youth and their Families	The South African College of Applied Psychology	1500	\N	\N
Fall	2021	Ghan	Natalia	Theresa Raphael-Grimm	School of Nursing	\N	NURS	864	Biopsychosocial Care 3: Psychiatric Mental Health Interventions in the Context of Relationships	Jonkoping University	1500	natalia.ghan@unc.edu	\N
Fall	2023	Lee	Nayeon	Maureen Baker	School of Nursing	\N	NURS	934	Clinical Scholarship and Professional Communication	St. Luke’s International University	1500	\N	\N
Fall	2021	Castro Fernandez 	Noel	Tom Linden	Hussman School of Journalism & Media	\N	MEJO	560	Environmental and Science Journalism	University of Navarra	1500	noelcasfer@unc.edu	\N
Spring	2022	Castro Fernandez 	Noel	Erin Siegal McIntyre	Hussman School of Media and Journalism	 	MEJO	553	Advanced Reporting	Universidad Autónoma de Baja California	1500	\N	\N
Fall	2022	Mino	Pablo	Joseph Czabovsky	Hussman School of Journalism and Media	\N	MEJO	531	Case Studies in Public Relations	Pontificia Universidad Católica de Chile	1500	\N	\N
Fall	2021	Brookie	Parker	Patricia Rosenmeyer	College of Arts & Sciences	Classics	CLAS	363H	Greek & Latin Poetry in Translation	Universidade de São Paulo	1500	pbrookie@live.unc.edu	\N
Fall	2020	Nguyen 	Phuong	Lien Truong	College of Arts & Sciences 	Art & Art History	ARTS	322	Narrative Painting	Vietnam University of Fine Arts	1500	\N	\N
Spring	2024	Garang Akau	Samuel	Raphael Birya	College of Arts & Sciences	Public Policy	SWAH	402	Elementary Kiswahili II	Pwani University	1500	\N	\N
Spring	2021	Levine	Sharon	Helyne Frederick	School of Education	Education	EDUC	475	Child and Family Health	St. George's University	1500	splevine@email.unc.edu	\N
Spring	2023	Wang	Shuguang	Yi Zhou	School of Education	\N	CHIN	306	Advanced Chinese II	Tianjin Normal University	1500	\N	\N
Fall	2023	Wang	Shuguang	Yi Zhou	School of Education	\N	CHIN	306	Advanced Chinese I	Tianjin Normal University	1500	\N	\N
Spring	2024	Wang	Shuguang	Dana Riger	School of Education	\N	EDUC	375	Identity & Sexuality	National Taiwan Normal University	1500	\N	\N
Fall	2024	Wang	Shuguang	Yi Zhou	School of Education	\N	CHIN	305	Advanced Chinese I	Tianjin Normal University	1500	\N	\N
Fall	2022	Bartels	Sophia	Vivian Go	Gillings School of Global Public Health	\N	HBEH	784	Implementation Science in Global Health	Hanoi Medical University	1500	\N	\N
Spring	2021	Priskos	Stefani	Patricia Sawin	College of Arts & Sciences 	American Studies	FOLK/ENGL	487	Everyday Stories 	University College Dublin	1500	spriskos@live.unc.edu	\N
Spring	2024	Elsayed	Tarek	Caroline Sibley	College of Arts & Sciences	Asian & Middle Eastern Studies	ARAB	306	Advanced Arabic	Mohammed VI Polytechnic University and Durham Technical Community College	1500	\N	\N
Spring	2023	Dsouza	Vinisha	Evi Bonilla	School of Nursing	\N	NURS	402	Foundations of Population Health and Global Health: Carolina Core IV	Australian Catholic University	750	\N	\N
Fall	2023	Dsouza	Vinisha Flavia	Theresa Raphael-Grimm	School of Nursing	\N	NURS	301	Foundations of Relationship-Centered Care and Diversity and Inclusion	Jönköping University	750	\N	\N
Fall	2023	Bian	Wenxin	Suja Davis	School of Nursing	\N	NURS	691	Honors in Nursing Part 1	Universidad de Monterrey	1500	\N	\N
Spring	2021	Piskačová	Zora	Chad Bryant	College of Arts & Sciences  	History	HIST	783	Readings in Russian and East European History	King's College London / Charles University	1500	zora.piskacova@unc.edu	\N
Fall	2022	Piskačová	Zora	Chad Bryant	College of Arts & Sciences	History	HIST	783	Readings in Russian and East European History	King's College London / Charles University	1500	\N	\N
\.


--
-- Name: faculty faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY ("Last Name", "First Name", "Semester Taught", "Course Title", "Cancelled");


--
-- Name: grad_student grad_student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grad_student
    ADD CONSTRAINT grad_student_pkey PRIMARY KEY ("Semester Taught", "Year Taught", "Last Name", "First Name", "Course", "Number");


--
-- PostgreSQL database dump complete
--

