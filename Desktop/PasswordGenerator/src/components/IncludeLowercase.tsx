import  { ChangeEvent } from "react";

type includelowercaseProps = {
  includelowercase: boolean  ;
  setIncludeLowercase: (include: boolean) => void;
};

const includeLowercase = ({includelowercase,setIncludeLowercase}: includelowercaseProps) => {

  const handleincludeLowercase = (event: ChangeEvent<HTMLInputElement>) => {
    setIncludeLowercase(!includelowercase);
  };


  return (
    <div className="mb-2">
      <input
        type="checkbox"
        id="includelowercase"
        checked={includelowercase}
        className="mr-2"
        onChange={handleincludeLowercase}
      />
      <label htmlFor="includelowercase">Include Lowercase Letters</label>
    </div>
  );
};

export default includeLowercase;
