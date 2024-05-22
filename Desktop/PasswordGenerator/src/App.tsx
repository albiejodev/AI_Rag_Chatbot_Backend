import  { useState } from "react";
import PasswordLength from "./components/PasswordLength";
import IncludeUppercase from "./components/IncludeUppercase";
import IncludeLowercase from "./components/IncludeLowercase";
import IncludeNumbers from "./components/IncludeNumbers";
import IncludeSymbols from "./components/IncludeSymbols";
import { generatePassword } from "./utils/generatePassword";
import {AiOutlineCopy} from 'react-icons/ai'


const App = () => {

  const [password, setPassword] = useState<string | null>(null);

  const [passwordlength, setPasswordlength] = useState<number>(4);

  const [includeuppercase, setIncludeUppercase] = useState<boolean>(true);

  const [includelowercase, setIncludeLowercase] = useState<boolean >(true);

  const [includeNumbers, setIncludeNumbers] = useState<boolean >(true);

  const [includeSymbols, setIncludeSymbols] = useState<boolean >(true);

  const handleGeneratePassword=()=>{
    const newPassword = generatePassword({length : passwordlength, includeuppercase, includelowercase, includeNumbers, includeSymbols});
    setPassword(newPassword);
  }

  const handleCopyClick=()=>{
    if(password){
      navigator.clipboard.writeText(password)
    }
  }

  return (
    
    <div className="font-FiraCode flex flex-col gap-4 justify-center items-center min-h-screen bg-black text-white">
          {
            password && (
              <div className="bg-gray-700  text-white px-4 py-2 break-all flex justify-between items-center w-[20rem] mb-4">
                <div className="text-xl">{password}</div>
                <button className="text-xl" onClick={handleCopyClick}>
                  <AiOutlineCopy/>
                </button>
              </div>
            )
          }
      <div className="w-[20rem] bg-gray-800 p-4">

        <PasswordLength passwordlength={passwordlength} setPasswordlength={setPasswordlength}/>

        <IncludeUppercase includeuppercase={includeuppercase} setIncludeUppercase={setIncludeUppercase} />

        <IncludeLowercase includelowercase={includelowercase} setIncludeLowercase={setIncludeLowercase} />

        <IncludeNumbers includeNumbers={includeNumbers} setIncludeNumbers={setIncludeNumbers}/>

        <IncludeSymbols includeSymbols={includeSymbols} setIncludeSymbols={setIncludeSymbols}/>

        <button className="px-4 py-2 bg-PastelGreen rounded-md shadow-md w-full border text-black font-bold border-solid hover:border-PastelGreen hover:text-PastelGreen hover:bg-BalticSea transition-all duration-300 uppercase" onClick={handleGeneratePassword}>generate</button>

      </div>
    </div>
  );
};

export default App;
