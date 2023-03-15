import React from 'react'
import Table from './Provence/table'

export default function Index() {

    return (
        <>
            <div className="content-wrapper">
                <div className="content-header">
                    <div className="container-fluid">
                        <div className="row">
                            <div className="col-12">
                                <div className="card">
                                    <div className="card-header">
                                        <h2>ຂໍ້ມູນແຂວງ ແລະ ເມືອງ</h2>
                                    </div>
                                </div>
                            </div>
                            <div className="col-md-6">
                                <Table/>
                                {/* /.card Proveince */}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
