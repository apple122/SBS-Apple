import axios from 'axios'
import React, { useEffect, useState } from 'react'
import Form from './form'
import useFuncations from './useFuncations'

export default function Table() {
    const {
        Input,
        GETAPI,
    } = useFuncations()

    return (
        <div className="card">
            <Form/>
            {Input}
            <div className="card-body table-responsive p-0">
                <table className="table table-hover text-nowrap">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>ຊື່ແຂວງ</th>
                            <th className="text-center">ຈັດການ</th>
                            <th className="text-center col-1">ສະແດງຂໍ້ມູນແຂວງ</th>
                        </tr>
                    </thead>

                    <tbody>
                        {GETAPI.filter((e) => e.is_active === true).map((item, index) => (
                            <tr key={index}>
                                <td>#{index+1}</td>
                                <td>{item.province}</td>
                                <td className="text-center">Active</td>
                                <td className="text-center col-1">Right</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    )
}
