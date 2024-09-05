import { AtSign, Plus, X } from "lucide-react";
import { FormEvent } from "react";
import { Button } from "./button";
import { useParams } from "react-router-dom";
import { api } from "../lib/axios";

interface InviteGuestsModalProps {
  closeGuestsModalt: () => void;
  emailsToInvite: string[];
  addNewEmailToInvite: (e: FormEvent<HTMLFormElement>) => void;
  removeEmailtoInvite: (emailToRemove: string) => void;
  shouldSendData?: boolean;
}

export function InviteGuestsModal({
  closeGuestsModalt,
  addNewEmailToInvite,
  emailsToInvite,
  removeEmailtoInvite,
  shouldSendData,
}: InviteGuestsModalProps) {
  const { tripId } = useParams();

  async function inviteNewGuests() {
    await api.post(`/trips/${tripId}/invites`, {
      name: "",
      email: emailsToInvite,
    });
    window.document.location.reload();
  }

  return (
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center">
      <div className="w-[640px] rounded-xl py-5 px-6 shadow-shape bg-zinc-900 space-y-5">
        <div className="space-y-2">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold">Selecionar convidados</h2>
            <button type="button">
              <X onClick={closeGuestsModalt} className="size-5 text-zinc-400" />
            </button>
          </div>
          <p className="text-sm text-zinc-400">
            Os convidados irão receber e-mails para confirmar a participação na
            viagem.
          </p>
        </div>
        <div className="flex flex-wrap gap-2">
          {emailsToInvite.map((email) => {
            return (
              <div
                key={email}
                className="py-1.5 px-2.5 rounded-md bg-zinc-800 flex items-center gap-2"
              >
                <span className="text-zinc-300">{email}</span>
                <button
                  type="button"
                  onClick={() => removeEmailtoInvite(email)}
                >
                  <X className="size-4 text-zinc-400" />
                </button>
              </div>
            );
          })}
        </div>

        <div className="w-full h-px bg-zinc-800"></div>

        <form
          onSubmit={addNewEmailToInvite}
          className="p-2.5 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2"
        >
          <div className="px-2 flex items-center flex-1 gap-2">
            <AtSign className="text-zinc-400" />
            <input
              type="text"
              name="email"
              placeholder="Digite o e-mail do convidado"
              className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
            />
          </div>
          <Button type="submit" variant="primary">
            Convidar
            <Plus className="size-5 text-lime-950" />
          </Button>
        </form>

        {shouldSendData && (
          <Button variant="primary" onClick={inviteNewGuests} size="full">
            Adicionar novos participantes
          </Button>
        )}
      </div>
    </div>
  );
}
