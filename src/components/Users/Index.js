import React from 'react'
import Table from './Content/Table'

export default function Index() {
    return (
        <>
            <div className="content-wrapper" id="edit">
                <div className="content-header">
                    <div className="container-fluid">
                        <div className="row">
                            <div className="col-12">
                                <div className="card">
                                    <div className="card-header">
                                        <h5>Users</h5>
                                    </div>
                                </div>
                            </div>

                            <Table />
                            
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
