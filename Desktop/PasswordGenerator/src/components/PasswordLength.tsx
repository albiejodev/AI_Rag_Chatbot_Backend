import React, { ChangeEvent } from 'react'

type PasswordLengthProps = {
  passwordlength : number
  setPasswordlength:(length:number)=>void
}


const PasswordLength = ({passwordlength , setPasswordlength} : PasswordLengthProps) => {


  const handlePasswordlengthChange = (event:ChangeEvent<HTMLInputElement>) =>{
    setPasswordlength(parseInt(event.target.value , 10))
  }
  return (
    <div className='mb-4'>
      <label className='flex items-center justify-between font-medium'>
        <div>Password Length</div>
        <div className='text-2xl text-PastelGreen'>{passwordlength}</div>
      </label>
      <input type='range' id="passwordLength" min="4" max="20" value={passwordlength} className='w-full appearance-none h-1' onChange={handlePasswordlengthChange}/>
    </div>
  )
}

export default PasswordLength