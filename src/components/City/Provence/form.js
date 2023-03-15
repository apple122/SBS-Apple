import axios from 'axios'
import React, { useState } from 'react'
import Swal from 'sweetalert2'
import useFuncations from './useFuncations'

export default function Form() {

    const {
        setformValues,
        SubProvine,
        refrest,
    } = useFuncations()

    function deleteProvince() {

    }

    return (
        <>
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
                            <button class="accordion-button collapsed" onClick={refrest} type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">ເພີມແຂວງ</button>
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
        </>
    )
}
