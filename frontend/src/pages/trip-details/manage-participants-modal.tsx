import { Mail, User, X } from "lucide-react";
import { FormEvent } from "react";
import { Button } from "../../components/button";

interface ConfirmTripModalProps {
  closeConfirmTripModal: () => void;
  createTrip: (e: FormEvent<HTMLFormElement>) => void;
  setOwnerName: (onwnerName: string) => void;
  setOwnerEmail: (onwnerEmail: string) => void;
}

export function ManageParticipantsModal({
  closeConfirmTripModal,
  createTrip,
  setOwnerName,
  setOwnerEmail,
}: ConfirmTripModalProps) {
  return (
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center">
      <div className="w-[640px] rounded-xl py-5 px-6 shadow-shape bg-zinc-900 space-y-5">
        <div className="space-y-2">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold">Adicionar participantes</h2>
            <button type="button">
              <X
                onClick={closeConfirmTripModal}
                className="size-5 text-zinc-400"
              />
            </button>
          </div>
          <p className="text-sm text-zinc-400">Inclua</p>
        </div>
        <div className="flex flex-wrap gap-2"></div>

        <form onSubmit={createTrip} className="space-y-3">
          <div className="h-14 px-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2 items-center">
            <User className="text-zinc-400 size-5" />
            <input
              name="name"
              placeholder="Seu nome completo"
              className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
              onChange={(event) => setOwnerName(event.target.value)}
            />
          </div>

          <div className="h-14 p-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2">
            <Mail className="text-zinc-400 size-5" />
            <input
              type="email"
              placeholder="Seu e-mail pessoal"
              className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
              onChange={(event) => setOwnerEmail(event.target.value)}
            />
          </div>

          <Button type="submit" variant="primary" size="full">
            Confirmar criação da viagem
          </Button>
        </form>
      </div>
    </div>
  );
}
