import React from "react";


export default function KeyStatistics() {
    return (
        <section className="keystats">
            <div className="keystats--content">
                <div className="keystats--item">
                    <div className="keystats--label">Departments Participating</div>
                    <div className="keystats--number">28</div>
                </div>
                <div className="keystats--item">
                    <div className="keystats--label">Courses Available</div>
                    <div className="keystats--number">100</div>
                </div>
                <div className="keystats--item">
                    <div className="keystats--label">Participating Schools</div>
                    <div className="keystats--number">50</div>
                </div>
                <div className="keystats--item">
                    <div className="keystats--label">Students Enrolled</div>
                    <div className="keystats--number">100</div>
                </div>
            </div>
        </section>
    );
}