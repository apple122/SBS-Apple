import React from 'react'
import useFunctions from './useFunctions'

export default function Table() {

    let {
        API
    } = useFunctions()

    return (
        <div className="col-md-12">
            <div className='card'>
                <div className="card-header display-flex">
                    <div className="col-md-4">
                        <h3 className="card-title">User ( <strong className='text-danger'></strong> )</h3>
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

                <div className="card-body table-responsive p-0">
                    <table className="table table-hover text-nowrap">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>UserName</th>
                                <th>email</th>
                                <th className="text-center">ຈັດການ</th>
                            </tr>
                        </thead>
                        <tbody>
                            {API.map((item, index) => (
                                <tr>
                                    <td>{index}</td>
                                    <td>{item.username}</td>
                                    <td>{item.email}</td>
                                    <td>
                                        <div className='btn-group'>
                                            <button>edit</button>
                                            <button>edit</button>
                                        </div>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>

                </div>
            </div>
            {/* /.card Proveince */}
        </div>
    )
}
