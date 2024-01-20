use freedb_Wuzzuf;

CREATE TABLE Company (
	CompanyName varchar(300) NOT NULL PRIMARY KEY,
    MinimumSize int NULL,
    MaximumSize int NULL,
    FoundationDate int NULL,
    Country varchar(35) NULL,
    City varchar(35) NULL,
    CompanyUrl varchar(500),
    CompanyDescription varchar(5000) null
);

CREATE TABLE Sector (
	SectorName varchar(70) NOT NULL PRIMARY KEY
);

CREATE TABLE CompanySector (
	CompanyName varchar(300) NOT NULL,
    SectorName varchar(70) NOT NULL,
    PRIMARY KEY(CompanyName, SectorName),
    FOREIGN KEY(CompanyName) references Company(CompanyName)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(SectorName) references Sector(SectorName)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Applicant (
	EmailAddress varchar(320) NOT NULL PRIMARY KEY,
    Username varchar(50) NULL,
    FName varchar(25) NOT NULL,
    MName varchar(25) NULL,
    LName varchar(25) NOT NULL,
    Gender char NOT NULL,
    Birthdate DATE NOT NULL, 
    PhoneNo char(14) NOT NULL,
    Nationality varchar(35) NOT NULL,
    GPA DECIMAL(3,2) Not NULL,
    EducationLevel varchar(35) NULL,
    CareerLevel varchar(35) NULL,
    Country varchar(35) NULL,
    City varchar(35) NULL
);

CREATE TABLE JobPost (
	CompanyName varchar(80) NOT NULL,
    JobTitle varchar(100) NOT NULL,
    DatePosted Date NOT NULL,
    JobType varchar(20) NOT NULL,
    Status varchar(10) not null,
    Country varchar(35) NULL,
    City varchar(35) NULL,
    Region varchar(35) NULL,
    MinimumExperience int NULL,
    MaximumExperience int NULL,
    MinimumSalary int NULL,
    MaximumSalary int NULL,
    EducationLevel varchar(35) NULL,
    CareerLevel varchar(35) NULL,
	JobDescription varchar(1024) NULL,
    JobRequirements varchar(1000) NULL,
    PRIMARY KEY(CompanyName, JobTitle, DatePosted)
);


CREATE TABLE AppliesFor (
	ApplicantEmail varchar(320) NOT NULL,
    CompanyName varchar(80) NOT NULL,
    JobTitle varchar(100) NOT NULL,
    DatePosted Date NOT NULL,
    ApplicationDate Date NOT NULL,
    TextualCoverLetter varchar(3000) NOT NULL,
    PRIMARY KEY(ApplicantEmail, CompanyName, JobTitle, DatePosted),
    FOREIGN KEY(ApplicantEmail) references Applicant(EmailAddress)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(CompanyName, JobTitle, DatePosted) references JobPost(CompanyName, JobTitle, DatePosted)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Skills (
	SkillName varchar(100) NOT NULL PRIMARY KEY
);

CREATE TABLE JobCategories (
	CategoryName varchar(70) NOT NULL PRIMARY KEY
);


CREATE TABLE JobPostSkills (
	CompanyName varchar(80) NOT NULL,
    JobTitle varchar(100) NOT NULL,
    DatePosted Date NOT NULL,
	SkillName varchar(100) NOT NULL,
    PRIMARY KEY(CompanyName, JobTitle, DatePosted, SkillName),
    FOREIGN KEY(CompanyName, JobTitle, DatePosted) references JobPost(CompanyName, JobTitle, DatePosted)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(SkillName) references Skills(SkillName)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE JobPostCategory (
	CompanyName varchar(80) NOT NULL,
    JobTitle varchar(100) NOT NULL,
    DatePosted Date NOT NULL,
	CategoryName varchar(70) NOT NULL,
    PRIMARY KEY(CompanyName, JobTitle, DatePosted, CategoryName),
    FOREIGN KEY(CompanyName, JobTitle, DatePosted) references JobPost(CompanyName, JobTitle, DatePosted)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(CategoryName) references JobCategories(CategoryName)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE ApplicantSkills (
    ApplicantEmail VARCHAR(320) NOT NULL,
    SkillName VARCHAR(100) NOT NULL,
    PRIMARY KEY (ApplicantEmail , SkillName),
    FOREIGN KEY (ApplicantEmail) REFERENCES Applicant (EmailAddress)
        ON UPDATE CASCADE ON DELETE CASCADE, 
    FOREIGN KEY (SkillName) REFERENCES Skills (SkillName)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE ApplicantJobCategory (
	ApplicantEmail varchar(320) NOT NULL,
    CategoryName varchar(70) NOT NULL,
    PRIMARY KEY(ApplicantEmail, CategoryName),
    FOREIGN KEY(ApplicantEmail) references Applicant(EmailAddress)
		ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(CategoryName) references JobCategories(CategoryName)
		ON UPDATE CASCADE ON DELETE CASCADE
);

Create Table ApplicantPassword(
	ApplicantEmail varchar(320) NOT NULL PRIMARY KEY,
    Password varchar(16) NOT NULL
);