import { Calendar, Clock, Tag, X } from "lucide-react";
import { Button } from "../../components/button";
import { FormEvent } from "react";
import { useParams } from "react-router-dom";
import { api } from "../../lib/axios";

interface CreateActivityModalProps {
  closeCreateActivityModal: () => void;
}

export function CreateActivityModal({
  closeCreateActivityModal,
}: CreateActivityModalProps) {
  const { tripId } = useParams();

  async function createActvity(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const data = new FormData(event.currentTarget);

    const title = data.get("title")?.toString();
    const day = data.get("day")?.toString();
    const occurs_at = data.get("occurs")?.toString();

    if (!occurs_at) {
      return;
    }

    if (!day) {
      return;
    }

    if (!title) {
      return;
    }
    console.log(day + "T" + occurs_at);
    const response = await api.post(`/trips/${tripId}/activities`, {
      title: title,
      occurs_at: day + "T" + occurs_at,
    });

    window.document.location.reload();
  }

  return (
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center">
      <div className="w-[640px] rounded-xl py-5 px-6 shadow-shape bg-zinc-900 space-y-5">
        <div className="space-y-2">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold">Cadastrar atividade</h2>
            <button type="button">
              <X
                onClick={closeCreateActivityModal}
                className="size-5 text-zinc-400"
              />
            </button>
          </div>
          <p className="text-sm text-zinc-400">
            Todos convidados podem visualizar as atividades.
          </p>
        </div>
        <div className="flex flex-wrap gap-2"></div>

        <form onSubmit={createActvity} className="space-y-3">
          <div className="h-14 px-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2 items-center">
            <Tag className="text-zinc-400 size-5" />
            <input
              name="title"
              placeholder="Qual a atividade?"
              className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
            />
          </div>
          <div className="flex items gap-2">
            <div className="flex-1 h-14 p-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2">
              <Calendar className="text-zinc-400 size-5" />
              <input
                type="date"
                name="day"
                placeholder="20 de Agosto"
                className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
              />
            </div>
            <div className="w-36 h-14 p-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2">
              <Clock className="text-zinc-400 size-5" />
              <input
                name="occurs"
                type="time"
                placeholder="11:00"
                className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
              />
            </div>
          </div>
          <Button type="submit" variant="primary" size="full">
            Salvar atividade
          </Button>
        </form>
      </div>
    </div>
  );
}
