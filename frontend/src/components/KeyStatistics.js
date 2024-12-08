import React, { useState, useEffect } from "react";

export default function KeyStatistics() {
    const [keyStats, setKeyStats] = useState({
        departmentsParticipating: 0,
        coursesAvailable: 0,
        participatingSchools: 0,
        studentsEnrolled: 0,
    });

    // Fetch key stats data on component mount
    useEffect(() => {
        fetch("http://localhost:8080/key-stats/")
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`KeyStats fetch error: ${response.statusText}`);
                }
                return response.json();
            })
            .then((data) => {
                setKeyStats({
                    departmentsParticipating: data.departments_participating,
                    coursesAvailable: data.courses_available,
                    participatingSchools: data.participating_schools,
                    studentsEnrolled: data.students_enrolled,
                });
            })
            .catch((error) => console.error("Error fetching KeyStats:", error));
    }, []);

    return (
        <section className="keystats">
            <div className="keystats--content">
                <div className="keystats--item">
                    <div className="keystats--label">Departments Participating</div>
                    <div className="keystats--number">{keyStats.departmentsParticipating}</div>
                </div>
                <div className="keystats--item">
                    <div className="keystats--label">Courses Available</div>
                    <div className="keystats--number">{keyStats.coursesAvailable}</div>
                </div>
                <div className="keystats--item">
                    <div className="keystats--label">Participating Schools</div>
                    <div className="keystats--number">{keyStats.participatingSchools}</div>
                </div>
                <div className="keystats--item">
                    <div className="keystats--label">Students Enrolled</div>
                    <div className="keystats--number">{keyStats.studentsEnrolled}</div>
                </div>
            </div>
        </section>
    );
}
