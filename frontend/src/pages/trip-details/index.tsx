import { Plus } from "lucide-react";
import { FormEvent, useState } from "react";
import { CreateActivityModal } from "./create-activity-modal";
import { ImportantLinks } from "./important-links";
import { Guests } from "./guests";
import { Actvities } from "./activities";
import { DestinationAndDateHeader } from "./destination-and-date-header";
import { Button } from "../../components/button";

export function TripDetailsPage() {
  const [isCreateActivityModalOpen, setIsCreateActivityModalOpen] =
    useState(false);

  const [emailsToInvite, setEmailsToInvite] = useState([]);

  function addNewEmailToInvite(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    const data = new FormData(e.currentTarget);
    const email = data.get("email");

    if (!email) {
      return;
    }

    if (emailsToInvite.includes(email)) {
      return;
    }

    setEmailsToInvite([...emailsToInvite, email]);

    e.currentTarget.reset();
  }

  function removeEmailtoInvite(emailToRemove: string) {
    const newEmailList = emailsToInvite.filter(
      (invited) => invited != emailToRemove
    );

    setEmailsToInvite(newEmailList);
  }

  function openCreateActivityModal() {
    setIsCreateActivityModalOpen(true);
  }

  function closeCreateActivityModal() {
    setIsCreateActivityModalOpen(false);
  }

  return (
    <div className="max-w-6xl px-6 py-10 mx-auto space-y-8">
      <DestinationAndDateHeader />
      <main className="flex gap-16 px-6">
        <div className="flex-1 space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-3xl font-semibold">Atividades</h2>
            <Button onClick={openCreateActivityModal} variant="primary">
              <Plus className="size-5 text-lime-950" />
              Cadastrar atividade
            </Button>
          </div>
          <Actvities />
        </div>
        <div className="w-80 space-y-6">
          <ImportantLinks />

          <div className="w-full h-px bg-zinc-800"></div>

          <Guests
            addNewEmailToInvite={addNewEmailToInvite}
            removeEmailtoInvite={removeEmailtoInvite}
            emailsToInvite={emailsToInvite}
          />
        </div>
      </main>

      {isCreateActivityModalOpen && (
        <CreateActivityModal
          closeCreateActivityModal={closeCreateActivityModal}
        />
      )}
    </div>
  );
}
