import axios from 'axios'
import url from './data'
import React, { useEffect, useReducer, useState } from 'react'
import Swal from 'sweetalert2'

const useFuncations = () => {

    const [reducer, setRedeuce] = useReducer(x => x + 1, 0)
    const [proPageN, setproPageN] = useState(1)

    const [GETAPIDIS, setAPIDIS] = useState([])
    useEffect(() => {

        axios.get(url.Mainurl + url.getdistrict + `&province=${DIs}`).then((res) => {
            setAPIDIS(res.data.results)
        })
    }, [reducer])


    const [InputDis, setformDis] = useState('')
    function SubDistrict() {
        setRedeuce()
        if (InputDis !== '') {
            axios.post(url.Mainurl + url.createdistric, {
                district: InputDis,
                is_active: true,
                province: (AlertD === false ? null : DIs)
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
                    title: 'ບັນທືກຂໍ້ມູນສຳເລັດ'
                })
            })
        }
    }

    const [loaddis, setLdis] = useState(false)
    const [datadis, setdatadis] = useState('')
    console.log(datadis)
    const [Bydis, setBydis] = useState('')
    function editdistrict(e) {
        setLdis(true)
        setdatadis(e)
        setBydis(e)
    }
    function subEditeDis() {
        setRedeuce()
        if (datadis !== '') {
            axios.patch(url.Mainurl + url.patchdistrict + Bydis.id, {
                district: datadis,
                is_active: true,
                province: Bydis.province.id,
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
                    title: 'ປ່ຽນແປ່ງຂໍ້ມູນສຳເລັດ'
                })
            })
        }
    }

    const [ loadedit, setloadwidt ] = useState(true)
    function cancel_dis() {
        setloadwidt(false)
    }
    
    function deldistrict(e) {
        Swal.fire({
            title: 'ທ່ານຕ້ອງການລົບຂໍ້ມູນນີ້ ຫຼື ບໍ່?',
            text: "ເມືອລົບແລ້ວຂໍ້ມູນຈະຍັງເກັບ ແຕ່ບໍ່ສາມາດນຳມາໃຊ້ໄດ້ອີກ!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'ລົບຂໍ້ມູນ!'
        }).then((result) => {
            if (result.isConfirmed) {
                axios.patch(url.Mainurl + url.patchdistrict + e, {
                    is_active: false
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
                        title: 'ລົບຂໍ້ມູນສຳເລັດ'
                    })
                })
            }
        })
    }


    return {
        GETAPIDIS,
        setformDis,
        SubDistrict,
        refrestDis,
        deldistrict,
        editdistrict,
        loaddis,
        cancel_dis,
        loadedit,
        datadis,
        setdatadis,
        subEditeDis,

        proPageN,
    }
}

export default useFuncations