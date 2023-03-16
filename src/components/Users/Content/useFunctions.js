import axios from 'axios'
import React, { useEffect, useState } from 'react'
import url from '../data'

export default function useFunctions() {
  
    const [ API, setAPI ] = useState([])
    useEffect(() => {
      axios.get(url.Mainurl + url.getusers).then((res) => {
        setAPI(res.data.results)
      })
    })

  return {
    API
  }
}
