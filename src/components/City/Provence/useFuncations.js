import axios from 'axios'
import url from '../data'
import React, { useEffect, useReducer, useState } from 'react'
import Swal from 'sweetalert2'

export default function useFuncations() {

    const [reducer, setRedeuce] = useReducer(x => x + 1, 0)
    const [GETAPI, setAPI] = useState([])
    useEffect(() => {
        axios.get(url.Mainurl + url.getproveince).then((res) => {
            setAPI(res.data.results)
        })
    }, [reducer])

    const [Input, setformValues] = useState('')
    function SubProvine() {
        setRedeuce()
        if (Input !== '') {
            axios.post(url.Mainurl + url.createprovence, {
                "province": Input,
                "is_active": true
            }).then((res) => {
                const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 3000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                })
                setRedeuce()
                Toast.fire({
                    icon: 'success',
                    title: 'ບນທືກຂໍ້ມູນສຳເລັດ'
                })
            })
        }
    }

    function refrest() {
        setRedeuce()
    }

    return {
        setformValues,
        SubProvine,
        Input,
        url,
        GETAPI,
        refrest,
    }
}
