import { CheckCircle2, CircleDashed, UserCog } from "lucide-react";
import { Button } from "../../components/button";
import { FormEvent, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { api } from "../../lib/axios";
import { InviteGuestsModal } from "../../components/invite-guests-modal";

interface ParticipantData {
  id: string;
  name: string | null;
  is_confirmed: boolean;
  email: string;
}

interface GuestsProps {
  emailsToInvite: string[];
  addNewEmailToInvite: (e: FormEvent<HTMLFormElement>) => void;
  removeEmailtoInvite: (emailToRemove: string) => void;
}

export function Guests({
  emailsToInvite,
  addNewEmailToInvite,
  removeEmailtoInvite,
}: GuestsProps) {
  const { tripId } = useParams();
  const [participants, setParticipants] = useState<
    ParticipantData[] | undefined
  >();
  const [isManageGuestsModalOpen, setIsManageGuestsModalOpen] = useState(false);

  function openManageGuestsModal() {
    setIsManageGuestsModalOpen(true);
  }

  function closeManageGuestsModal() {
    setIsManageGuestsModalOpen(false);
  }

  useEffect(() => {
    api
      .get(`/trips/${tripId}/participants`)
      .then((response) => setParticipants(response.data.participants));
  }, [tripId]);

  return (
    <div className="space-y-6">
      <h2 className="font-semibold text-xl">Convidados</h2>
      <div className="space-y-5">
        {participants?.map((participant, index) => {
          return (
            <div
              key={participant.id}
              className="flex items-center justify-between gap-4"
            >
              <div className="space-y-1.5 flex-1">
                <span className="font-medium text-zinc-100 block">
                  {participant.name ?? `Convidado ${index}`}
                </span>
                <span className="text-sm text-zinc-400 block truncate">
                  {participant.email}
                </span>
              </div>
              {participant.is_confirmed ? (
                <CheckCircle2 className="size-5 shrink-0 text-green-400" />
              ) : (
                <CircleDashed className="text-zinc-400 size-5" />
              )}
            </div>
          );
        })}
      </div>

      <Button variant="secondary" onClick={openManageGuestsModal} size="full">
        <UserCog className="size-5" />
        Gerenciar convidados
      </Button>

      {isManageGuestsModalOpen && (
        <InviteGuestsModal
          addNewEmailToInvite={addNewEmailToInvite}
          closeGuestsModalt={closeManageGuestsModal}
          emailsToInvite={emailsToInvite}
          removeEmailtoInvite={removeEmailtoInvite}
          shouldSendData={true}
        />
      )}
    </div>
  );
}
