import { ChangeEvent } from "react";

type includeUppercaseProps = {
  includeuppercase: boolean ;
  setIncludeUppercase: (include: boolean) => void;
};

const IncludeUppercase = ({includeuppercase,setIncludeUppercase}: includeUppercaseProps) => {


  const handleincludeUppercase = (event: ChangeEvent<HTMLInputElement>) => {
    setIncludeUppercase(!includeuppercase);
  };


  return (
    <div className="mb-2">
      <input
        type="checkbox"
        id="includeUppercase"
        checked={includeuppercase}
        className="mr-2"
        onChange={handleincludeUppercase}
      />
      <label htmlFor="includeuppercase">Include Uppercase Letters</label>
    </div>
  );
};

export default IncludeUppercase;
