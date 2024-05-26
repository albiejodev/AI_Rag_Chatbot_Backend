import React, { ChangeEvent } from 'react'



type includeNumberProps = {
  includeNumbers: boolean ;
  setIncludeNumbers: (include: boolean) => void;
};


const IncludeNumbers = ({includeNumbers , setIncludeNumbers} : includeNumberProps) => {

  const handleincludeLowercase = (event: ChangeEvent<HTMLInputElement>) => {
    setIncludeNumbers(!includeNumbers);
  };


  return (

    <div className="mb-2">
    <input
      type="checkbox"
      id="includeNumber"
      checked={includeNumbers}
      className="mr-2"
      onChange={handleincludeLowercase}
    />
    <label htmlFor="includeNumber">Include Numbers</label>
  </div>
  )
}

export default IncludeNumbers