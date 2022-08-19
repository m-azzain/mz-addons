/** @odoo-module **/

import { escapeAndCompactTextContent } from '@mail/js/utils';
import { registerClassPatchModel, registerInstancePatchModel } from'@mail/model/model_core';

/*patch name can be any name; but shouldn't be reused**/
registerInstancePatchModel('mail.composer_view', 'mail_ext/static/src/models/composer_view_15.js', {
    /**
     * Open the full composer modal.
     */
    async openFullComposer() {
        const attachmentIds = this.composer.attachments.map(attachment => attachment.id);
        const context = {
            default_attachment_ids: attachmentIds,
            default_body: escapeAndCompactTextContent(this.composer.textInputContent),
            default_is_log: this.composer.isLog,
            default_model: this.composer.activeThread.model,
            default_partner_ids: this.composer.recipients.map(partner => partner.id),
            default_res_id: this.composer.activeThread.id,
            mail_post_autofollow: true,

            from_full_composer: true,
        };

        const action = {
            type: 'ir.actions.act_window',
            res_model: 'mail.compose.message',
            view_mode: 'form',
            views: [[false, 'form']],
            target: 'new',
            context: context,
        };
        const composer = this.composer;
        const options = {
            on_close: () => {
                if (!composer.exists()) {
                    return;
                }
                composer._reset();
                if (composer.activeThread) {
                    composer.activeThread.loadNewMessages();
                }
            },
        };
        await this.env.bus.trigger('do-action', { action, options });
    }
});

