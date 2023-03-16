import React from 'react'
import useFuncations from '../useFuncations'

export default function District() {

    let {
        GETAPIDIS,
        Loadding,
        setformDis,
        SubDistrict,
        refrestDis,
        deldistrict,
        editdistrict,
        cancel_dis,
        loadedit,
        datadis,
        setdatadis,
        subEditeDis,

        proPageN,
    } = useFuncations()

    let xpro = 23 * (proPageN - 1) + 1

    return (
        <div className="col-md-12">
            <div className='card'>
                <div className="card-header display-flex">
                    <div className="col-md-4">
                        <h3 className="card-title">ເມືອງທັງຫມົດ ( <strong className='text-danger'></strong> )</h3>
                    </div>
                    <div className="col-md-8">
                        <div className="input-group input-group-sm">
                            <input type="text" name="table_search" className="form-control float-right" placeholder="ຄົ້ນຫາດ້ວຍຊື່ເມື່ອງ..."/>
                            <select name="table_search" className="form-control float-right">
                                
                            </select>
                            <div className="input-group-append">
                                <button type="submit" className="btn btn-default">
                                    <i className="fas fa-search" />
                                </button>
                            </div>
                            <div className="input-group-text bg-green">
                                <button class="accordion-button collapsed" onClick={refrestDis} type="button" data-bs-toggle="collapse" data-bs-target='#collapseOne' aria-expanded="false" aria-controls="collapseTwo">ເພີມເມື່ອງ</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="accordion" id="accordionExample">
                    <div id="collapseOne" class="accordion-collapse collapse id Example" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <div className="form-group">
                                <label htmlFor="exampleInputEmail1">ຊື່ເມືອງ</label>
                                <div className="input-group">
                                    <input type="search" className="form-control" name='name' onChange={(e) => setformDis(e.target.value)} placeholder="ປ້ອນຊື່ເມືອງ" required />
                                    <span className="input-group-text btn bg-green" onClick={SubDistrict}><i class="bi bi-plus-lg"></i> | ບັນທືກຂໍ້ມູນເມືອງ</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div className='w-100 card-body' hidden={loadedit == true ? false : true}>
                    <div class="accordion-body">
                        <div className="form-group">
                            <label htmlFor="exampleInputEmail1">ແກ້ໄຂຊື່ເມືອງ</label>
                            <div className="input-group">
                                <input type="search" id='inputedite' value={datadis.district} className="form-control" name='name' onChange={(e) => setdatadis(e.target.value)} placeholder="ປ້ອນຊື່ເມືອງ" required />
                                <span className="input-group-text btn bg-green" onClick={subEditeDis}><i class="bi bi-plus-lg"></i> | ບັນທືກ</span>
                                <span className="input-group-text btn bg-danger" onClick={cancel_dis}>Cancel</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="card-body table-responsive p-0">
                    <table className="table table-hover text-nowrap">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>ຊື່ເມືອງ</th>
                                <th>ຊື່ແຂວງ</th>
                                <th className="text-center">ຈັດການ</th>
                            </tr>
                        </thead>

                        <tbody>
                            {GETAPIDIS.filter((e) => e.is_active === true).map((item, index) => (
                                <tr key={index}>
                                    <td>#{index + 1}</td>
                                    <td>{item.district}</td>
                                    <td>{item.province.province}</td>
                                    <td className="text-center">
                                        <div className='btn-group'>
                                            <a href='#edit' onClick={() => editdistrict(item)}><label for='inputedite' className='btn btn-sm btn-primary'><i class="bi bi-pencil-square"></i> ແກ້ໄຂຂໍ້ມູນ</label></a>
                                            <label for='inputedite' className='btn btn-sm btn-danger' onClick={() => deldistrict(item.id)}><i class="bi bi-trash3-fill"></i> ລົບຂໍ້ມູນ</label>
                                        </div>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                    {GETAPIDIS.filter((e) => e.is_active === true).length === 0 ? <h1 className='text-center my-3'>ບໍ່ມີຂໍ້ມູນ {Loadding.province}</h1> : ""}
                </div>
            </div>
            {/* /.card District */}
        </div>
    )
}
