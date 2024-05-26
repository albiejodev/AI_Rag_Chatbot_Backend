import  { ChangeEvent } from 'react'



type includeSymbolProps = {
  includeSymbols: boolean  ;
  setIncludeSymbols: (include: boolean) => void;
};


const IncludeSymbols = ({includeSymbols , setIncludeSymbols} : includeSymbolProps) => {

  const handleincludesymbols = (event: ChangeEvent<HTMLInputElement>) => {
    setIncludeSymbols(!includeSymbols);
  };


  return (

    <div className="mb-2">
    <input
      type="checkbox"
      id="includeNumber"
      checked={includeSymbols}
      className="mr-2"
      onChange={handleincludesymbols}
    />
    <label htmlFor="includeNumber">Include Symbols</label>
  </div>
  )
}

export default IncludeSymbols