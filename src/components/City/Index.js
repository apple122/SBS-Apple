import React, { useState } from 'react'
import useFuncations from './useFuncations'
import './provice.css'
import Province from './province/Province'
import District from './district/District'

const Index = () => {
    let {
        setformValues,
        SubProvine,
        refrest,
        GETAPI,
        GETAPIDIS,
        Loadding,
        delprovice,
        ListDis,
        AlertD,
        setformDis,
        SubDistrict,
        refrestDis,
        deldistrict,
        proLegn,
        editprovice,
        loadedit,
        cancel_pro,
        Byidpro,
        setBypro,
        EditProvine,
        editdistrict,
        loaddis,
        cancel_dis,
        datadis,
        setdatadis,
        subEditeDis,

        Nextpro,
        Blackpro,
        proPage,
        proPageN,

        clickdrop,
        droppro,
    } = useFuncations()

    let xpro = 23 * (proPageN - 1) + 1

    const [paget, setpagetrue] = useState('province')
    function pagetrue(e) {
        setpagetrue(e)
    }

    return (
        <>
            <div className="content-wrapper" id="edit">
                <div className="content-header">
                    <div className="container-fluid">
                        <div className="row">
                            <div className="col-12">
                                <div className="card">
                                    <div className="card-header">
                                        <h2>ຂໍ້ມູນແຂວງ ແລະ ເມືອງ</h2>
                                    </div>
                                    <ul class="nav nav-tabs pt-2 px-2">
                                        <li class="nav-item">
                                            <button class={`nav-link ${paget == 'province' ? 'active' : ''}`} onClick={() => pagetrue('province')}>ຂໍ້ມູນແຂວງ ( <strong className='text-danger'>{proLegn}</strong> )</button>
                                        </li>
                                        <li class="nav-item">
                                            <button class={`nav-link ${paget == 'district' ? 'active' : ''}`} onClick={() => pagetrue('district')}>district</button>
                                        </li>
                                        <li class="nav-item">
                                            <button class={`nav-link ${paget == 'village' ? 'active' : ''}`} onClick={() => pagetrue('village')}>village</button>
                                        </li>
                                    </ul>
                                </div>
                            </div>

                            {paget === 'province' ? <Province/> : ''}
                            {paget === 'district' ? <District/> : ''}

                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Index