import {
  MapPin,
  Calendar,
  ArrowRight,
  UserRoundPlus,
  Settings2,
} from "lucide-react";
import { useState } from "react";

export function App() {
  const [isGuestsInputOpen, setIsGuestsInputOpen] = useState(false);
  const [isGuestsModalOpen, setIsGuestsModalOpen] = useState(true);

  function openGuestsInput() {
    setIsGuestsInputOpen(true);
  }

  function closeGuestsInput() {
    setIsGuestsInputOpen(false);
  }

  function openGuestsModal() {
    setIsGuestsModalOpen(true);
  }

  function closeGuestsModalt() {
    setIsGuestsModalOpen(false);
  }

  return (
    <div className="h-screen flex items-center justify-center bg-pattern bg-no-repeat bg-center">
      <div className="max-w-3xl w-full px-6 text-center space-y-10">
        <div className="flex flex-col items-center gap-3">
          <img src="./public/logo.svg" alt="plann.er" />
          <p className="text-zinc-300 text-lg">
            Convide seus amigos e planeje sua próxima viagem!
          </p>
        </div>
        <div className="space-y-4">
          <div className="h-16 px-4 bg-zinc-900 rounded-xl gap-3 flex items-center shadow-shape">
            <div className="flex items-center gap-2 flex-1">
              <MapPin className="size-5 text-zinc-400" />
              <input
                type="text"
                placeholder="para onde você vai?"
                className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
                disabled={isGuestsInputOpen}
              />
            </div>
            <div className="flex items-center gap-2">
              <Calendar className="size-5 text-zinc-400" />
              <input
                type="text"
                placeholder="Quando?"
                className="bg-transparent text-lg placeholder-zinc-400 w-40 outline-none"
                disabled={isGuestsInputOpen}
              />
            </div>

            <div className="w-px h-6 bg-zinc-800"></div>
            {isGuestsInputOpen ? (
              <button
                onClick={closeGuestsInput}
                className="bg-zinc-800 text-zinc-200 rounded-lg px-5 py-2 font-medium flex items-center gap-2  hover:bg-zinc-700"
              >
                Alterar local/data
                <Settings2 className="size-5" />
              </button>
            ) : (
              <button
                onClick={openGuestsInput}
                className="bg-lime-300 text-lime-950 rounded-lg px-5 py-2 font-medium flex items-center gap-2  hover:bg-lime-400"
              >
                Continuar
                <ArrowRight className="size-5 text-lime-950" />
              </button>
            )}
          </div>
          {isGuestsInputOpen ? (
            <div className="h-16 px-4 bg-zinc-900 rounded-xl gap-3 flex items-center shadow-shape">
              <button className="flex items-center gap-2 flex-1 text-left">
                <UserRoundPlus className="size-5 text-zinc-400" />
                <span className="text-lg text-zinc-400  flex-1">
                  Quem estará na viagem?
                </span>
              </button>

              <div className="w-px h-6 bg-zinc-800"></div>
              <button className="bg-lime-300 text-lime-950 rounded-lg px-5 py-2 font-medium flex items-center gap-2  hover:bg-lime-400">
                Confirmar viagem
                <ArrowRight className="size-5 text-lime-950" />
              </button>
            </div>
          ) : null}
        </div>
        <p className="text-sm text-zinc-500">
          Ao planejar sua viagem pela plann.er você automaticamente concorda{" "}
          <br /> com nossos{" "}
          <a
            href="#"
            className="text-zinc-300 underline"
            target="_blank"
            rel="noopener noreferrer"
          >
            termos de uso
          </a>{" "}
          e{" "}
          <a
            href="#"
            className="text-zinc-300 underline"
            target="_blank"
            rel="noopener noreferrer"
          >
            políticas de privacidade
          </a>
          .
        </p>
      </div>
    </div>
  );
}
