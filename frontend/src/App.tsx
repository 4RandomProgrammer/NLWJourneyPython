import { MapPin, Calendar, ArrowRight } from "lucide-react";

export function App() {
  return (
    <div className="h-screen flex items-center justify-center bg-pattern bg-no-repeat bg-center">
      <div className="max-w-3xl w-full px-6 text-center space-y-10">
        <p className="text-zinc-300 text-lg">
          Convide seus amigos e planeje sua próxima viagem!
        </p>

        <div className="h-16 px-4 bg-zinc-900 rounded-xl gap-3 flex items-center shadow-shape">
          <div className="flex items-center gap-2 flex-1">
            <MapPin className="size-5 text-zinc-400" />
            <input
              type="text"
              placeholder="para onde você vai?"
              className="bg-transparent text-lg placeholder-zinc-400 outline-none"
            />
          </div>
          <div className="flex items-center gap-2">
            <Calendar className="size-5 text-zinc-400" />
            <input
              type="text"
              placeholder="Quando?"
              className="bg-transparent text-lg placeholder-zinc-400 w-40 outline-none"
            />
          </div>

          <div className="w-px h-6 bg-zinc-800"></div>

          <button className="bg-lime-300 text-lime-950 rounded-lg px-5 py-2 font-medium flex items-center gap-2  hover:bg-lime-400">
            Continuar
            <ArrowRight className="size-5 text-lime-950" />
          </button>
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
