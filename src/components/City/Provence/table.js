import axios from 'axios'
import React, { useEffect, useState } from 'react'
import url from '../data'

export default function Table() {
    const [Input, setformValues] = useState('')
    const [ GETAPI, setAPI ] = useState([])
    useEffect(() => {
        axios.get(url.Mainurl + url.getproveince).then((res) => {
            setAPI(res.data.results)
        })
    }, [])

    function SubProvine() {

    }

    function deleteProvince() {

    }

    return (
        <div className="card">
            <div className="card-header display-flex">
                <div className="col-md-4">
                    <h3 className="card-title">ແຂວງທັງຫມົດ ( <strong className='text-danger'></strong> )</h3>
                </div>
                <div className="col-md-8">
                    <div className="input-group input-group-sm">
                        <input type="text" name="table_search" className="form-control float-right" placeholder="ຄົ້ນຫາດ້ວຍຊື່ແຂວງ..." />
                        <div className="input-group-append">
                            <button type="submit" className="btn btn-default">
                                <i className="fas fa-search" />
                            </button>
                        </div>
                        <div className="input-group-text bg-green">
                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">ເພີມແຂວງ</button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="accordion" id="accordionExample">
                <div id="collapseTwo" class="accordion-collapse collapse idExample" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        <div className="form-group">
                            <label htmlFor="exampleInputEmail1">ຊື່ແຂວງ</label>
                            <div className="input-group">
                                <input type="search" className="form-control" name='name' onChange={(e) => setformValues(e.target.value)} placeholder="ປ້ອນຊື່ແຂວງ" required />
                                <span className="input-group-text btn bg-green" onClick={SubProvine}><i class="bi bi-plus-lg"></i> | ບັນທືກຂໍ້ມູນແຂວງ</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            {/* /.card-header */}
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
