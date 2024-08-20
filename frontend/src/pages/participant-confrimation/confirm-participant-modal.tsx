import { Mail, User, X } from "lucide-react";
import { FormEvent } from "react";
import { Button } from "../../components/button";

interface ConfirmTripModalProps {
  closeConfirmParticipantModal: () => void;
  createParticipant: (e: FormEvent<HTMLFormElement>) => void;
  setParticipantName: (onwnerName: string) => void;
  setParticipantEmail: (onwnerEmail: string) => void;
}

export function ConfirmParticipantModal({
  closeConfirmParticipantModal,
  createParticipant,
  setParticipantName,
  setParticipantEmail,
}: ConfirmTripModalProps) {
  return (
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center">
      <div className="w-[640px] rounded-xl py-5 px-6 shadow-shape bg-zinc-900 space-y-5">
        <div className="space-y-2">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold">Confirmar participação</h2>
            <button type="button">
              <X
                onClick={closeConfirmParticipantModal}
                className="size-5 text-zinc-400"
              />
            </button>
          </div>
          <p className="text-sm text-zinc-400">
            Você foi convidado(a) para participar de uma viagem para{" "}
            <span className="font-semibold text-zinc-100">
              {" "}
              Florianópolis, Brasil
            </span>{" "}
            nas datas de{" "}
            <span className="font-semibold text-zinc-100">
              16 a 27 de Agosto de 2025
            </span>
            .
          </p>
          <p className="text-sm text-zinc-400">
            Para confirmar sua presença na viagem, preencha os dados abaixo:
          </p>
        </div>
        <div className="flex flex-wrap gap-2"></div>

        <form onSubmit={createParticipant} className="space-y-3">
          <div className="h-14 px-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2 items-center">
            <User className="text-zinc-400 size-5" />
            <input
              name="name"
              placeholder="Seu nome completo"
              className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
              onChange={(event) => setParticipantName(event.target.value)}
            />
          </div>

          <div className="h-14 p-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2">
            <Mail className="text-zinc-400 size-5" />
            <input
              type="email"
              placeholder="Seu e-mail"
              className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
              onChange={(event) => setParticipantEmail(event.target.value)}
            />
          </div>

          <Button type="submit" variant="primary" size="full">
            Confirmar minha presença
          </Button>
        </form>
      </div>
    </div>
  );
}
